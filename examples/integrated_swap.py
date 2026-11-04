from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "python"))

from battery_swap.integrated_simulation import Battery, Inventory, SimUAV, StationSupervisor

uav = SimUAV()
inventory = Inventory([
    Battery("spent-001", 0.18, slot=0),
    Battery("charged-001", 0.95, slot=1),
])
result = StationSupervisor(uav, inventory).run_swap()
print(f"success={result.success} final_state={result.final_state.value} events={len(result.events)}")
for event in result.events:
    print(event["event"], event.get("battery_id", ""))
