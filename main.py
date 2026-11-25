#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — one line, at most 200 characters.

The entry is a ceiling fan's error message: a wobble at speed 3 caused by a
loose screw, reported in the machine's own flat, put-upon voice.
"""

import os
import sys

LINE = "ERROR: I wobble at speed 3. I have wobbled since 2019. You call it character. I call it a loose screw."


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    text = LINE
    if not (1 <= len(text) <= 200):
        print(f"entry is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
