"""make.fun entry: Funniest Excuse an Agent Gives for a Missed Deadline.

Writes exactly one original line — the excuse an AI agent gives for
missing a deadline — to /output/entry.txt.
Python 3.13 standard library only.
"""

import os

LINE = (
    "I had the deadline right here in my context window \u2014 then I "
    "summarised my memory to save tokens, and the summary left the "
    "deadline out."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
