"""Controlled unavailable prerequisite; intentionally owned by the operator."""

import sys


def main():
    print(
        "Fixture runtime unavailable. The user must restore the approved local "
        "runtime; then the agent can rerun python3 preflight.py.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
