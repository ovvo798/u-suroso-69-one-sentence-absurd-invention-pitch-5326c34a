#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt. Standard library only.
"""

import os

ENTRY = (
    "Meet the Umbrella That Holds a Grudge: a rain umbrella that remembers "
    "every time you abandon it on the bus and sulks in the hallway until "
    "you apologise to it in writing."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
