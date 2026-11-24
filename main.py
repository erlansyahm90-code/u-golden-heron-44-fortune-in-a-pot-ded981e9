"""A single fortune for a potted plant, written out to a file.

This little program has one job: put a kind, hopeful prediction for a
houseplant into the place the judges will read it from. The words stay
inside the competition's length window, and the file is written as plain
UTF-8 with nothing extra trailing behind the text.
"""

from pathlib import Path

# The fortune itself: a gentle prediction about the plant's own future.
ENTRY = (
    "Your roots will find the good soil, your leaves will catch the "
    "morning sun, and the cat will finally leave you alone."
)

# The competition only accepts fortunes between one and 120 characters.
# Anything outside that window fails the gate before the judges see it.
assert 1 <= len(ENTRY) <= 120, "fortune must be 1-120 characters"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    # Write the text exactly as it stands, no newline at the end.
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
