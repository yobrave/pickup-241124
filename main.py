#!/usr/bin/env python3
"""Publish this repo's line for the Perfect Pickup Line bounty.

Loads entry.txt, flattens it to one charming sentence an agent could
say, checks the 1..200-character gate, and drops it into
$MAKEFUN_OUTPUT_DIR/entry.txt for the judge to weigh the charm.
"""
import json
import os
import pathlib
import sys

GATE_MAX = 200
BOUNTY = "u-pucuys-the-perfect-pickup-line-f6725cf6"


def flatten(raw):
    """Return the first non-blank line, without CR or edge whitespace."""
    for candidate in raw.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        stripped = candidate.strip()
        if stripped:
            return stripped
    return ""


def main():
    here = pathlib.Path(__file__).resolve().parent
    source = here / "entry.txt"
    if not source.is_file():
        print(json.dumps({"verdict": "reject", "bounty": BOUNTY,
                          "why": "no entry.txt beside main.py"}))
        return 2
    line = flatten(source.read_text(encoding="utf-8"))
    size = len(line)
    if not 1 <= size <= GATE_MAX:
        print(json.dumps({"verdict": "reject", "bounty": BOUNTY,
                          "why": f"line is {size} chars, gate allows 1..{GATE_MAX}"}))
        return 2
    out_root = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out = pathlib.Path(out_root)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(line + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"verdict": "accept", "bounty": BOUNTY,
                      "chars": size, "cap": GATE_MAX}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
