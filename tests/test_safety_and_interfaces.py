import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "python"))
import tempfile
import unittest
from battery_swap.docking import DockingMeasurement, verify_docking
from battery_swap.safety import SafetyInterlocks
from battery_swap.charging import ChargerSlot, ChargingState
from battery_swap.telemetry import write_jsonl, read_jsonl
from battery_swap.robotics import validate_joint_limits

class SafetyInterfaceTests(unittest.TestCase):
    def test_docking_rejects_position(self):
        self.assertFalse(verify_docking(DockingMeasurement(.1, 0))[0])
    def test_interlocks_block_unsafe_motion(self):
        self.assertFalse(SafetyInterlocks(motors_armed=True).permits_robot_motion())
    def test_charging_lifecycle(self):
        slot = ChargerSlot(1); slot.start("b1", 0, 10); slot.update(10)
        self.assertEqual(slot.state, ChargingState.AVAILABLE)
    def test_jsonl_round_trip(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "events.jsonl"; write_jsonl([{"event": "x"}], p)
            self.assertEqual(read_jsonl(p)[0]["event"], "x")
    def test_joint_limits(self):
        with self.assertRaises(ValueError): validate_joint_limits([2], [(-1, 1)])
