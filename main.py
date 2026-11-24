#!/usr/bin/env python3
"""Worst AI Advice entry: writes one line of the worst advice an AI
could give to /output/entry.txt (max 140 characters, plain text)."""

import os

ADVICE = (
    "As your AI assistant, I recommend deleting System32 to free up "
    "space \u2014 it worked great in my training data."
)

def main() -> None:
    # Gate: entry must be 1-140 characters of UTF-8 text, not only
    # whitespace. Keep the file to the bare line (no trailing newline)
    # so the byte count is exactly the line's length.
    assert 1 <= len(ADVICE) <= 140, f"entry is {len(ADVICE)} chars"
    assert ADVICE.strip(), "entry must not be only whitespace"
    assert "\n" not in ADVICE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ADVICE)

if __name__ == "__main__":
    main()
