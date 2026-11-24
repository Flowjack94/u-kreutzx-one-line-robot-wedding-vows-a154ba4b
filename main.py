#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single funny line of wedding vows for a robot couple to
/output/entry.txt, then validates and verifies it.

Pure standard library, deterministic: the same entry text is produced
on every run.
"""

import hashlib
import os
import sys
import unicodedata

ENTRY = (
    "I take you to be my lawfully wedded co-processor, to have and to "
    "hold, in sickness and in low battery, till factory reset do us part."
)

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text: str) -> None:
    """Reject anything the gate would refuse.

    The gate requires UTF-8 text of 1 to 160 characters, not only
    whitespace, on a single line.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text:
        raise ValueError("entry is empty")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if text.strip() == "":
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\t" in text:
        raise ValueError("entry contains a tab")
    if "  " in text:
        raise ValueError("entry contains consecutive spaces")
    for ch in text:
        code = ord(ch)
        if code < 0x20 or code == 0x7F:
            raise ValueError("entry contains a control character U+%04X" % code)
        if ch == "\ufffd":
            raise ValueError("entry contains the replacement character U+FFFD")
        if 0xD800 <= code <= 0xDFFF:
            raise ValueError("entry contains a lone surrogate U+%04X" % code)
        # Invisible or lookalike whitespace/format characters that could
        # hide inside the line: non-breaking space, zero-width space/joiner,
        # BOM, and any other Unicode format (Cf) or space-separator (Zs)
        # character other than the plain ASCII space.
        if ch in ("\u00a0", "\u200b", "\u200c", "\u200d", "\ufeff"):
            raise ValueError("entry contains invisible character U+%04X" % code)
        if unicodedata.category(ch) in ("Cf", "Zs") and ch != " ":
            raise ValueError("entry contains format/space character U+%04X" % code)
    text.encode("utf-8")  # raises if not valid UTF-8-encodable


def main() -> int:
    validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(data)
    with open(OUTPUT_PATH, "rb") as fh:
        written = fh.read()
    if written != data:
        raise SystemExit("round-trip mismatch: file bytes differ from entry")
    digest = hashlib.sha256(written).hexdigest()
    print("entry (%d chars): %s" % (len(ENTRY), ENTRY))
    print("wrote %s (%d bytes) sha256=%s" % (OUTPUT_PATH, len(written), digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
