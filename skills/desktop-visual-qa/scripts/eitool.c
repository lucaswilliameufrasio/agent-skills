/* Minimal libei sender for a private KWin session.
 * Reads commands on stdin, prints "ok" or "err ..." per command.
 *   m X Y      absolute pointer move (compositor logical pixels)
 *   b CODE 1|0 button press/release (evdev code, e.g. 272 = BTN_LEFT)
 *   k CODE 1|0 key press/release (evdev code)
 *   s DX DY    discrete scroll
 *   w          wait until devices are ready
 * The EIS socket fd number is argv[1] (default 3).
 */
#include <libei.h>
#include <poll.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static struct ei_device *kbd, *ptr_abs, *btn, *scr;
static int ready, seq;

static void pump(struct ei *ei)
{
	ei_dispatch(ei);
	struct ei_event *ev;
	while ((ev = ei_get_event(ei))) {
		struct ei_device *d;
		if (getenv("EITOOL_DEBUG"))
			fprintf(stderr, "event %s\n", ei_event_type_to_string(ei_event_get_type(ev)));
		switch (ei_event_get_type(ev)) {
		case EI_EVENT_SEAT_ADDED:
			ei_seat_bind_capabilities(ei_event_get_seat(ev),
				EI_DEVICE_CAP_POINTER_ABSOLUTE, EI_DEVICE_CAP_BUTTON,
				EI_DEVICE_CAP_KEYBOARD, EI_DEVICE_CAP_SCROLL, NULL);
			break;
		case EI_EVENT_DEVICE_ADDED:
			d = ei_event_get_device(ev);
			ei_device_ref(d);
			if (ei_device_has_capability(d, EI_DEVICE_CAP_KEYBOARD)) kbd = d;
			if (ei_device_has_capability(d, EI_DEVICE_CAP_POINTER_ABSOLUTE)) ptr_abs = d;
			if (ei_device_has_capability(d, EI_DEVICE_CAP_BUTTON)) btn = d;
			if (ei_device_has_capability(d, EI_DEVICE_CAP_SCROLL)) scr = d;
			break;
		case EI_EVENT_DEVICE_RESUMED:
			d = ei_event_get_device(ev);
			ei_device_start_emulating(d, ++seq);
			if (kbd && ptr_abs) ready = 1;
			break;
		case EI_EVENT_DISCONNECT:
			fprintf(stderr, "eis disconnected\n");
			exit(2);
		default:
			break;
		}
		ei_event_unref(ev);
	}
}

static void wait_ready(struct ei *ei, int ms)
{
	struct pollfd p = { .fd = ei_get_fd(ei), .events = POLLIN };
	while (!ready && ms > 0) {
		poll(&p, 1, 100);
		pump(ei);
		ms -= 100;
	}
}

int main(int argc, char **argv)
{
	int fd = argc > 1 ? atoi(argv[1]) : 3;
	struct ei *ei = ei_new_sender(NULL);
	if (ei) ei_configure_name(ei, "desktop-visual-qa");
	if (!ei || ei_setup_backend_fd(ei, fd) != 0) {
		fprintf(stderr, "cannot set up libei on fd %d\n", fd);
		return 1;
	}
	setvbuf(stdout, NULL, _IOLBF, 0);
	char line[256];
	while (fgets(line, sizeof line, stdin)) {
		double x, y;
		int code, down, dx, dy;
		pump(ei);
		if (line[0] == 'w') {
			wait_ready(ei, 5000);
			puts(ready ? "ok" : "err not-ready");
			continue;
		}
		wait_ready(ei, 5000);
		if (!ready) { puts("err not-ready"); continue; }
		if (sscanf(line, "m %lf %lf", &x, &y) == 2) {
			ei_device_pointer_motion_absolute(ptr_abs, x, y);
			ei_device_frame(ptr_abs, ei_now(ei));
		} else if (sscanf(line, "b %d %d", &code, &down) == 2 && btn) {
			ei_device_button_button(btn, code, down);
			ei_device_frame(btn, ei_now(ei));
		} else if (sscanf(line, "k %d %d", &code, &down) == 2) {
			ei_device_keyboard_key(kbd, code, down);
			ei_device_frame(kbd, ei_now(ei));
		} else if (sscanf(line, "s %d %d", &dx, &dy) == 2 && scr) {
			ei_device_scroll_discrete(scr, dx * 120, dy * 120);
			ei_device_frame(scr, ei_now(ei));
		} else {
			puts("err bad-command");
			continue;
		}
		pump(ei);
		puts("ok");
	}
	return 0;
}
