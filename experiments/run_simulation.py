"""Run deterministic simulated trials and write machine-readable evidence."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "python"))
from battery_swap.integrated_simulation import Battery, Inventory, SimUAV, StationSupervisor
from battery_swap.telemetry import write_jsonl

events = []
for index in range(5):
    result = StationSupervisor(SimUAV(), Inventory([Battery("spent-001", .1, slot=0), Battery(f"charged-{index}", .95, slot=1)])).run_swap()
    events.extend({**event, "trial": index, "evidence_type": "simulation"} for event in result.events)
write_jsonl(events, Path(__file__).parent / "integration" / "simulation_events.jsonl")
print(f"wrote {len(events)} simulation events")
