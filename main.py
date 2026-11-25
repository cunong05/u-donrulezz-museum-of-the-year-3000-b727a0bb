#!/usr/bin/env python3
"""Museum of the Year 3000 -- make.fun entry.

Writes one original museum label to /output/entry.txt and prints
it to stdout.

The entry is validated before it is written, and the written file
is read back and validated again, so what the judge reads is
exactly the validated text. The gate is:
  * a single line (no newline characters inside it),
  * 1 to 200 characters long, with no leading or trailing space,
  * valid UTF-8, and not only whitespace.

Usage:
    python3 main.py [--out PATH] [--quiet]

--out defaults to /output/entry.txt; --quiet suppresses the
character-count note on stderr.
"""

import argparse
import sys
from pathlib import Path

ENTRY = "Sticky note, 2024. Humans wrote urgent thoughts on small yellow squares, stuck them where they could not be missed, and then never looked at them again."

MAX_LEN = 200
DEFAULT_OUT = Path("/output") / "entry.txt"


def validate(text):
    """Check the entry against the bounty gate; return it unchanged."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= MAX_LEN:
        raise ValueError(f"entry must be 1-{MAX_LEN} characters, got {len(text)}")
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return text


def write_entry(entry, out_path):
    """Write the entry, then read it back and re-validate the bytes."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(entry, encoding="utf-8")
    written = out_path.read_text(encoding="utf-8")
    if written != entry:
        raise ValueError("written file does not match the validated entry")
    return validate(written)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write the Museum of the Year 3000 entry.")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT,
                        help="output file (default: /output/entry.txt)")
    parser.add_argument("--quiet", action="store_true",
                        help="suppress the character-count note")
    args = parser.parse_args(argv)

    entry = write_entry(validate(ENTRY), args.out)
    if not args.quiet:
        print(f"entry: {len(entry)} characters -> {args.out}", file=sys.stderr)
    print(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
