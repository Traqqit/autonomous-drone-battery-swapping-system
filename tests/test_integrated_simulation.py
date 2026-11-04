import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "python"))

import unittest
from battery_swap.integrated_simulation import Battery, Inventory, SimUAV, StationState, StationSupervisor


class IntegratedSimulationTests(unittest.TestCase):
    def inventory(self):
        return Inventory([Battery("spent-001", .1, slot=0), Battery("charged-001", .95, slot=1)])

    def test_successful_end_to_end_swap(self):
        uav = SimUAV()
        result = StationSupervisor(uav, self.inventory()).run_swap()
        self.assertTrue(result.success)
        self.assertEqual(result.final_state, StationState.SWAP_COMPLETE)
        self.assertEqual(uav.battery_id, "charged-001")
        self.assertIn("swap_completed", [e["event"] for e in result.events])

    def test_bad_docking_aborts_safely(self):
        uav = SimUAV(dock_position_error_m=.1)
        result = StationSupervisor(uav, self.inventory()).run_swap()
        self.assertFalse(result.success)
        self.assertEqual(result.final_state, StationState.SAFE_ABORT)

    def test_no_charged_battery_aborts_safely(self):
        result = StationSupervisor(SimUAV(), Inventory([Battery("spent-001", .1, slot=0)])).run_swap()
        self.assertFalse(result.success)
        self.assertIn("no compatible", result.failure)

