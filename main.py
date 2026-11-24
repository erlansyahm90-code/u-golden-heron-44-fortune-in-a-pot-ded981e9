"""Fortune in a Pot — make.fun entry.

Writes a single-line fortune to /output/entry.txt.
The fortune is a one-liner (1-120 characters) for the
u-golden-heron-44-fortune-in-a-pot-ded981e9 bounty.
"""

import os

ENTRY = (
    # The fortune itself: 108 characters, within the 1-120 gate.
    "Your roots will find good soil, your leaves will catch the sun, "
    "and Biscuit stops eating you after 19 tries."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the entry line to /output/entry.txt (UTF-8)."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
