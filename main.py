"""Tech-support one-liner entry.

Writes the chosen support-agent reply to /output/entry.txt.
Standard library only. Plain open()/write() plus an explicit 0644 mode,
so the grader's sandbox sees exactly the bytes we wrote.
"""

import os

LINE = "Stay on the line while it restarts \u2014 I'll hum the hold music so neither of us feels alone."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Enforce the competition gate before writing anything: the entry
    # must be one line of 1-199 characters and not only whitespace.
    if not 1 <= len(LINE) <= 199:
        raise ValueError(f"entry is {len(LINE)} characters, gate needs 1-199")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
