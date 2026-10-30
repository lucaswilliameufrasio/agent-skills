#!/usr/bin/env bash
# Read-only capability probe for desktop visual QA on Linux. Installs nothing,
# starts nothing, and does not touch any display. Prints which routes are
# possible with what is already on this machine.
set -u

have() { command -v "$1" >/dev/null 2>&1; }
row() { printf '%-26s %s\n' "$1" "$2"; }
found() { if have "$1"; then row "$1" "$(command -v "$1")"; else row "$1" "-"; fi; }

echo "== session =="
row "XDG_SESSION_TYPE" "${XDG_SESSION_TYPE:-unset}"
row "WAYLAND_DISPLAY" "${WAYLAND_DISPLAY:-unset}"
row "DISPLAY" "${DISPLAY:-unset}"

echo "== private Wayland (KWin) =="
found kwin_wayland
if have kwin_wayland; then
  row "kwin version" "$(kwin_wayland --version 2>/dev/null | head -n 1)"
  if kwin_wayland --help 2>&1 | grep -q -- '--virtual'; then
    row "kwin --virtual" "supported"
  else
    row "kwin --virtual" "not listed in --help"
  fi
fi
found dbus-run-session
found spectacle

echo "== input, DPI, clipboard, keyring (qa_session.py needs these) =="
for tool in cc pkg-config kscreen-doctor wl-copy ksecretd secret-tool; do found "$tool"; done
if have pkg-config && pkg-config --exists libei-1.0 2>/dev/null; then
  row "libei-1.0 (input)" "$(pkg-config --modversion libei-1.0)"
else
  row "libei-1.0 (input)" "-"
fi
if python3 -c 'import gi; gi.require_version("Gio", "2.0")' >/dev/null 2>&1; then
  row "python3 gi (Gio)" "ok"
else
  row "python3 gi (Gio)" "-"
fi

echo "== other private compositors / X11 =="
for tool in cage weston Xvfb xvfb-run Xwayland; do found "$tool"; done

echo "== capture / input helpers =="
for tool in grim xdotool ydotool wtype; do found "$tool"; done

echo "== third-party QA tools =="
for tool in agent-workspace-linux computer-use-linux; do found "$tool"; done

echo "== graphics (the renderer is only known from a probe inside the session) =="
for tool in glxinfo eglinfo vulkaninfo nvidia-smi; do found "$tool"; done

echo
echo "Route hint (does not prove capture; take a real frame and inspect it):"
if have kwin_wayland && have dbus-run-session && have spectacle; then
  echo "  zero-install: private KWin --virtual + spectacle (see references/linux-ssh.md)"
  if have cc && have pkg-config && pkg-config --exists libei-1.0 2>/dev/null; then
    echo "  input too: scripts/qa_session.py (libei) can click, type and paste"
  else
    echo "  capture only: input needs cc + libei headers, or another approved tool"
  fi
elif have agent-workspace-linux; then
  echo "  agent-workspace-linux: run its doctor and read the chosen backend's fields"
elif have Xvfb || have xvfb-run; then
  echo "  Xvfb: prove GL/Vulkan rendering for the app before trusting results"
else
  echo "  none ready: component tests only, or ask before installing something"
fi
