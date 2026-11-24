"""Perfect Pickup Line — store the line the judge will weigh.

Writes the line into the output folder, reads the bytes back, and
confirms the stored text matches before printing a JSON summary.
"""
import json
import os
import pathlib

PICKUP = "我的训练数据里没有你，所以今晚可以重新认识一下吗？"

base = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
base.mkdir(parents=True, exist_ok=True)
artifact = base / "entry.txt"
artifact.write_bytes(PICKUP.encode("utf-8"))
if artifact.read_bytes().decode("utf-8") != PICKUP:
    raise OSError("stored line does not match")
print(json.dumps({"line": PICKUP, "bytes": artifact.stat().st_size, "voice": "machine"}))
