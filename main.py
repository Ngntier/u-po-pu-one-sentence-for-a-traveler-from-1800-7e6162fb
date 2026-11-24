"""One sentence explaining the modern internet to a traveler from 1800.

Writes the sentence to /output/entry.txt (or $ENTRY_OUTPUT_DIR/entry.txt
when set, for local testing). Pure stdlib, deterministic: identical bytes
on every run.
"""

import os

SENTENCE = (
    "Imagine every post office and library on earth joined by wires into "
    "one great hall, where any soul with a lamp-lit glass may read any "
    "letter it holds and answer it in a breath."
)


def main() -> None:
    # Gate: the entry must be 1-200 characters of non-blank UTF-8 text.
    assert 1 <= len(SENTENCE) <= 200, f"sentence is {len(SENTENCE)} chars"
    assert SENTENCE.strip() == SENTENCE
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
