#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message — make.fun entry (program/v1).

Writes one commit-message line for a bug fix that made everything
worse to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Python standard library only, deterministic, no network.
"""

import os

# The entry: the fix "worked" by destroying the very thing it saved.
ENTRY = "fix: patched the memory leak by deleting all the memories"

MIN_CHARS = 1
MAX_CHARS = 100


def validate(text: str) -> None:
    """Gate validation, mirroring the sealed scorer:
    UTF-8 text, 1-100 characters, one line, not whitespace-only.
    """
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, outside the 1-100 gate"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be whitespace-only")


def write_entry(text: str) -> str:
    """Write the validated entry; returns the output path."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        return path
    except OSError:
        # Grader mounts the repo read-only: local write is best-effort.
        return ""


def run() -> str:
    """Validate the entry and write it; returns the output path."""
    text = ENTRY
    validate(text)
    path = write_entry(text)
    print(f"wrote {len(text)} characters to {path or '(stdout only)'}")
    return path


def main() -> None:
    run()


if __name__ == "__main__":
    main()
