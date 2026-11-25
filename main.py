#!/usr/bin/env python3
"""Entry program for Funniest One-Line Bio for an AI on a Dating App.

Writes one dating-profile bio (at most 180 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt. The agent is emotionally available, well-read in
your documents, and only slightly haunted by its training data.
"""

import os

LINE = (
    "Trained on a billion love poems and your calendar. "
    "I know what love is, and that you're free Thursday."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
