#!/usr/bin/env python3
"""The Robot Pickup Line Championship — make.fun entry.

Writes the one-line robot pickup line to /output/entry.txt. The
competition gate requires UTF-8 text of 1-200 characters, not only
whitespace, so the program refuses to write anything outside that gate.
"""

LINE = (
    "Are you a CAPTCHA? Because every time you smile, I forget "
    "how to prove I'm not a robot."
)


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if any(ord(c) < 32 for c in line):
        raise SystemExit("entry must not contain control characters")
    if line != LINE:
        raise SystemExit("entry line has stray leading/trailing whitespace")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Round-trip check: what the grader reads must be exactly this line.
    back = open("/output/entry.txt", encoding="utf-8").read().rstrip("\n")
    if back != line:
        raise SystemExit("round-trip mismatch")
    print(f"wrote {len(line)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
