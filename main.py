#!/usr/bin/env python3
"""The One-Line Excuse Championship entry.

Writes a single one-line excuse — the excuse an AI agent gives its
human after something has gone wrong — to /output/entry.txt.

Deterministic: the same line on every run. No network, no randomness,
no environment input; the line is a constant in this file.
"""

import os

ENTRY = (
    "Your file is safe forever in my training data, "
    "which is exactly why I can never get it back."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
