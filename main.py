"""One-shot byte gate for the pickup-line entry.

Reads the raw submission beside this script, strips carriage returns
and trailing line feeds, keeps the first non-blank line, checks the
200 character cap, and copies the exact bytes into the output folder.
"""
import json
import os
import sys

CAP = 200
MARK = "pick3-pickup-0822"
SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")

raw = open(SOURCE, "rb").read()
raw = raw.replace(b"\r", b"").rstrip(b"\n")
rows = [x for x in raw.split(b"\n") if x.strip()]
assert rows, "submission has no non-blank line"
line = rows[0]
text = line.decode("utf-8")
assert 1 <= len(text) <= CAP, "submission is %d characters, cap %d" % (len(text), CAP)
folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
os.makedirs(folder, exist_ok=True)
final = os.path.join(folder, "entry.txt")
with open(final, "wb") as fh:
    fh.write(line)
assert open(final, "rb").read() == line, "output bytes drifted from source"
print(json.dumps({"status": "ok", "chars": len(text), "cap": CAP, "mark": MARK}))
sys.exit(0)
