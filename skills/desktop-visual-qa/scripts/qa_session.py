#!/usr/bin/env python3
"""Run a native app in a private KWin (Wayland) session and drive it.

Needs only tools shipped with Plasma plus python3-gobject, a C compiler and
libei headers (for input). Installs nothing, never touches the user's session:
private XDG_RUNTIME_DIR, private D-Bus, and (default) private HOME/XDG dirs.

  qa_session.py --out DIR [--size WxH] [--output-scale N] [--env K=V]... \
                [--real-home] [--keyring] --steps FILE -- APP [ARGS...]

Step file, one command per line ('#' comments):
  wait SECONDS | shot NAME | move X Y | click X Y | rclick X Y | dclick X Y
  key CHORD (Tab, Return, ctrl+a, shift+Tab) | type TEXT (US ASCII)
  paste TEXT (private clipboard, keeps Unicode) | scroll DX DY | note TEXT
  sh COMMAND (background helper, e.g. secret-tool to trigger the wallet wizard)
  output-scale N (change scale mid-run; prefer --output-scale N before launch)
Coordinates are compositor logical pixels (screenshot pixels / scale).
"""
import argparse, os, shutil, signal, subprocess, sys, tempfile, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
BTN = {"left": 272, "right": 273}
KEYS = {
    "esc": 1, "escape": 1, "backspace": 14, "tab": 15, "return": 28, "enter": 28,
    "ctrl": 29, "shift": 42, "alt": 56, "space": 57, "up": 103, "left": 105,
    "right": 106, "down": 108, "home": 102, "end": 107, "pageup": 104,
    "pagedown": 109, "delete": 111, "f1": 59, "f2": 60, "f3": 61, "f4": 62, "f5": 63,
}
for i, c in enumerate("1234567890"):
    KEYS[c] = 2 + i
for row, start in (("qwertyuiop", 16), ("asdfghjkl", 30), ("zxcvbnm", 44)):
    for i, c in enumerate(row):
        KEYS[c] = start + i
PLAIN = {" ": "space", "\n": "return", "-": 12, "=": 13, "[": 26, "]": 27, ";": 39,
         "'": 40, "`": 41, "\\": 43, ",": 51, ".": 52, "/": 53}
SHIFTED = {"_": 12, "+": 13, "{": 26, "}": 27, ":": 39, '"': 40, "~": 41, "|": 43,
           "<": 51, ">": 52, "?": 53, "!": 2, "@": 3, "#": 4, "$": 5, "%": 6,
           "^": 7, "&": 8, "*": 9, "(": 10, ")": 11}


def log(msg):
    print(f"[qa] {msg}", flush=True)


class Input:
    def __init__(self, fd, helper):
        self.p = subprocess.Popen([helper, str(fd)], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                  pass_fds=[fd], text=True)

    def send(self, line):
        self.p.stdin.write(line + "\n"); self.p.stdin.flush()
        reply = self.p.stdout.readline().strip()
        if reply != "ok":
            raise RuntimeError(f"input '{line}' -> {reply or 'no reply'}")

    def key(self, code, down): self.send(f"k {code} {int(down)}")

    def chord(self, spec):
        parts = [p.lower() for p in spec.split("+")]
        codes = [KEYS[p] for p in parts]
        for c in codes: self.key(c, 1)
        for c in reversed(codes): self.key(c, 0)
        time.sleep(0.15)

    def type(self, text):
        for ch in text:
            if ch.isupper() or ch in SHIFTED:
                code = SHIFTED.get(ch) or KEYS[ch.lower()]; shift = True
            else:
                code = PLAIN.get(ch, KEYS.get(ch)); shift = False
                if isinstance(code, str): code = KEYS[code]
            if code is None:
                raise ValueError(f"cannot type {ch!r}; use paste")
            if shift: self.key(KEYS["shift"], 1)
            self.key(code, 1); self.key(code, 0)
            if shift: self.key(KEYS["shift"], 0)
            time.sleep(0.02)

    def click(self, x, y, button="left", n=1):
        self.send(f"m {x} {y}"); time.sleep(0.1)
        for _ in range(n):
            self.send(f"b {BTN[button]} 1"); self.send(f"b {BTN[button]} 0"); time.sleep(0.08)
        time.sleep(0.2)


_BUS = None  # KWin drops the EIS client when the requesting D-Bus connection closes


def eis_fd():
    global _BUS
    from gi.repository import Gio, GLib
    _BUS = conn = Gio.bus_get_sync(Gio.BusType.SESSION)
    res, fds = conn.call_with_unix_fd_list_sync(
        "org.kde.KWin", "/org/kde/KWin/EIS/RemoteDesktop", "org.kde.KWin.EIS.RemoteDesktop",
        "connectToEIS", GLib.Variant("(i)", (7,)), GLib.VariantType("(hi)"),
        Gio.DBusCallFlags.NONE, 10000, None, None)
    return os.dup(fds.get(res.unpack()[0]))


def set_output_scale(env, value):
    """Real fractional scale through KDE output management (kscreen-doctor)."""
    import re
    listing = subprocess.run(["kscreen-doctor", "-o"], env=env, capture_output=True, text=True,
                             timeout=20).stdout
    m = re.search(r"Output: \d+ (\S+)", re.sub(r"\x1b\[[0-9;]*m", "", listing))
    if not m:
        raise RuntimeError("kscreen-doctor found no output")
    subprocess.run(["kscreen-doctor", f"output.{m.group(1)}.scale.{value}"], env=env,
                   check=True, capture_output=True, timeout=20)
    log(f"output {m.group(1)} scale {value}")
    time.sleep(1.5)


def shot(out, name, env):
    path = out / f"{name}.png"
    r = subprocess.run(["spectacle", "-b", "-n", "-f", "-o", str(path)], env=env,
                       capture_output=True, text=True, timeout=30)
    if not path.exists() or path.stat().st_size == 0:
        raise RuntimeError(f"capture failed: {r.stderr.strip()[:200]}")
    size = ""
    try:
        from PIL import Image
        size = " %dx%d" % Image.open(path).size
    except Exception:
        pass
    log(f"shot {path}{size}")


def inner(a):
    env = os.environ.copy()
    out = Path(a.out)
    w, h = a.size.split("x")
    kwin = subprocess.Popen(["kwin_wayland", "--virtual", "--socket", "qa0", "--width", w,
        "--height", h, "--no-lockscreen", "--no-global-shortcuts"],
        stdout=open(out / "kwin.log", "w"), stderr=subprocess.STDOUT)
    procs = [kwin]
    try:
        sock = Path(env["XDG_RUNTIME_DIR"]) / "qa0"
        for _ in range(80):
            if sock.exists(): break
            time.sleep(0.25)
        else:
            raise RuntimeError("kwin socket did not appear; see kwin.log")
        env.update(WAYLAND_DISPLAY="qa0", WINIT_UNIX_BACKEND="wayland", QT_QPA_PLATFORM="wayland")
        env.pop("DISPLAY", None)
        time.sleep(1.5)
        if a.output_scale:  # before the app starts, like a HiDPI monitor
            set_output_scale(env, a.output_scale)
        inp = Input(eis_fd(), a.helper); procs.append(inp.p)
        inp.send("w")
        if a.keyring:  # private Secret Service; its first-use wallet wizard is driven by steps
            ks = subprocess.Popen(["ksecretd"], env=env, stdout=open(out / "ksecretd.log", "w"),
                                  stderr=subprocess.STDOUT)
            procs.append(ks); time.sleep(2)
        app_env = dict(env)
        for kv in a.env: k, v = kv.split("=", 1); app_env[k] = v
        app = subprocess.Popen(a.app, env=app_env, stdout=open(out / "app.log", "w"),
                               stderr=subprocess.STDOUT)
        procs.append(app)
        time.sleep(a.settle)
        if app.poll() is not None:
            raise RuntimeError(f"app exited early with {app.returncode}; see app.log")
        log(f"app pid {app.pid} alive")
        for raw in Path(a.steps).read_text().splitlines():
            line = raw.strip()
            if not line or line.startswith("#"): continue
            cmd, _, rest = line.partition(" ")
            if app.poll() is not None:
                raise RuntimeError(f"app died before '{line}' (code {app.returncode})")
            if cmd == "wait": time.sleep(float(rest))
            elif cmd == "shot": shot(out, rest, env)
            elif cmd == "move": inp.send("m " + rest)
            elif cmd in ("click", "rclick", "dclick"):
                x, y = rest.split()
                inp.click(x, y, "right" if cmd == "rclick" else "left", 2 if cmd == "dclick" else 1)
            elif cmd == "key": inp.chord(rest)
            elif cmd == "type": inp.type(rest)
            elif cmd == "paste":
                subprocess.Popen(["wl-copy", "--", rest], env=env); time.sleep(0.4)
                inp.chord("ctrl+v")
            elif cmd == "scroll": inp.send("s " + rest)
            elif cmd == "output-scale": set_output_scale(env, rest)
            elif cmd == "sh":  # background helper in the private session (e.g. secret-tool)
                procs.append(subprocess.Popen(rest, shell=True, env=env, stdin=subprocess.DEVNULL,
                                              stdout=open(out / "sh.log", "a"), stderr=subprocess.STDOUT))
            elif cmd == "note": log(rest)
            else: raise ValueError(f"unknown step: {line}")
            time.sleep(0.3)
        log("steps done")
    finally:
        for p in reversed(procs):
            if p.poll() is None:
                p.terminate()
        for p in procs:
            try: p.wait(5)
            except subprocess.TimeoutExpired: p.kill()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True); ap.add_argument("--steps", required=True)
    ap.add_argument("--size", default="1360x860", help="physical framebuffer WxH")
    ap.add_argument("--env", action="append", default=[]); ap.add_argument("--real-home", action="store_true")
    ap.add_argument("--keyring", action="store_true", help="start a private ksecretd (Secret Service)")
    ap.add_argument("--output-scale"); ap.add_argument("--settle", type=float, default=5); ap.add_argument("--inner", action="store_true")
    ap.add_argument("--helper"); ap.add_argument("app", nargs=argparse.REMAINDER)
    a = ap.parse_args()
    a.app = [x for x in a.app if x != "--"] if a.app[:1] == ["--"] else a.app
    if not a.app: ap.error("app command required after --")
    Path(a.out).mkdir(parents=True, exist_ok=True)
    if a.inner:
        return inner(a)
    rt = tempfile.mkdtemp(prefix="kq.", dir="/tmp"); os.chmod(rt, 0o700)  # short: socket limit
    try:
        helper = os.path.join(rt, "eitool")
        cc = subprocess.run(["sh", "-c", f"cc -O1 -o {helper} {HERE}/eitool.c $(pkg-config --cflags --libs libei-1.0)"])
        if cc.returncode: sys.exit("cannot build eitool (need cc + libei headers)")
        env = os.environ.copy(); env["XDG_RUNTIME_DIR"] = rt
        if not a.real_home:
            home = os.path.join(rt, "home"); os.makedirs(home + "/.config")
            env.update(HOME=home, XDG_CONFIG_HOME=home + "/.config",
                       XDG_DATA_HOME=home + "/.local/share", XDG_CACHE_HOME=home + "/.cache")
        env.pop("DISPLAY", None); env.pop("WAYLAND_DISPLAY", None)
        argv = ["dbus-run-session", "--", sys.executable, __file__, "--inner", "--out", a.out,
                "--steps", a.steps, "--size", a.size, "--settle", str(a.settle),
                "--output-scale", a.output_scale or "",
                *(["--keyring"] if a.keyring else []),
                "--helper", helper] + sum((["--env", e] for e in a.env), []) + ["--"] + a.app
        sys.exit(subprocess.run(argv, env=env, timeout=600).returncode)
    finally:
        shutil.rmtree(rt, ignore_errors=True)


if __name__ == "__main__":
    main()
