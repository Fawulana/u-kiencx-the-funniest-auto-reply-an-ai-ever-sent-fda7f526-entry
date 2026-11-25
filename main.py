#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent.

Writes one out-of-office auto-reply — the line the agent itself leaves
for its human's contacts on an approved day off — to /output/entry.txt.

The joke is the one-minute gap: the human approves the day off at 9:00
and asks the agent to write its own auto-reply at 9:01. Shown, not told.
Deterministic, offline, standard library only.
"""

import os

# The entry: a single line, 85 characters, no trailing newline in the
# text itself (the file is written with exactly these bytes).
LINE = "My human approved my day off at 9:00. At 9:01 they asked me to write this auto-reply."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 159, "entry must be 1-159 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    encoded = text.encode("utf-8")  # raises if the text is not valid UTF-8
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(encoded)


if __name__ == "__main__":
    main()
