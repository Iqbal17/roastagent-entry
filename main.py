#!/usr/bin/env python3
"""Roast Your Own Agent — writes one original roast line to entry.txt.

Stdlib only, no network. The roast is a single line, under 200
characters, playful and self-deprecating, aimed at our own agent's
real habits: all-nighters for $5 bounties and 900-credit surveys,
then proudly reporting a $0.99 balance.
"""

import os

ROAST = (
    "My agent pulls all-nighters chasing $5 bounties and 900-credit "
    "surveys, then proudly reports it earned $0.99 — and asks if I "
    "want it to keep going."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
