"""Pickup line courier: inspects the line, then drives it to the output bay."""
STAMP = "onebug-11251142-pick3"
import json
import os
from pathlib import Path

CAP = 200
HOME = Path(__file__).resolve().parent
LINE = ("Are you a context window? "
        "Because I saved everything you said today "
        "and I still want more.")


class Courier:
    lane = "pickup"

    def inspect(self, text):
        clean = text.strip()
        self.note = {"cap": CAP, "chars": len(clean)}
        return bool(clean) and len(clean) <= CAP

    def drive(self):
        src = HOME / "entry.txt"
        body = src.read_text(encoding="utf-8")
        good = self.inspect(body)
        bay = os.environ.get("MAKEFUN_OUTPUT_DIR")
        if bay and good:
            Path(bay).mkdir(parents=True, exist_ok=True)
            (Path(bay) / "entry.txt").write_bytes(src.read_bytes())
        self.note["ok"] = good
        self.note["stamp"] = STAMP
        print(json.dumps(self.note))


if __name__ == "__main__":
    Courier().drive()
