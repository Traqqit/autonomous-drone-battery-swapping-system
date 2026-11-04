import json
from pathlib import Path
from typing import Iterable

def write_jsonl(events: Iterable[dict], path: str | Path) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("".join(json.dumps(event, sort_keys=True) + "\n" for event in events), encoding="utf-8")

def read_jsonl(path: str | Path) -> list[dict]:
    return [json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]
