#!/usr/bin/env python3
"""Everyday Wonder — one surprising sentence about an ordinary moment.

Stdlib only. Writes a single line to entry.txt in MAKEFUN_OUTPUT_DIR
(default /output).
"""

import os

ENTRY = (
    "The vending machine gave me two chocolate bars for one coin, "
    "and I walked away feeling chosen by a god with low standards."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
