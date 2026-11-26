"""One Star, Written in Sap entry: a maple leaves a one-star review.

Writes the entry line to /output/entry.txt. Standard library only.
"""

import os

ENTRY = (
    "One star. They tapped my sap for pancakes, then blamed the tree "
    "when the bottle leaked all over the kitchen table."
)


def main():
    # Contract: one funny line, under 200 characters, single line.
    assert 30 <= len(ENTRY) < 200, f"entry length {len(ENTRY)} out of band"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
