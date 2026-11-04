import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "python"))
import unittest
import numpy as np
from battery_swap.kinematics import Arm
from battery_swap.trajectory import smoothstep_trajectory
from battery_swap.swap_sequence import State, simulate_swap

class TestArm(unittest.TestCase):
    def test_straight_horizontal(self):
        a = Arm()
        xyz = a.tool_position([0,0,0,0])
        np.testing.assert_allclose(xyz, [a.upper+a.forearm+a.tool,0,a.shoulder_height], atol=1e-12)

    def test_base_rotation(self):
        a = Arm()
        p = a.tool_position([np.pi/2,0,0,0])
        self.assertAlmostEqual(p[0],0,places=12)
        self.assertAlmostEqual(p[1],a.upper+a.forearm+a.tool)

    def test_trajectory_endpoints(self):
        a = np.zeros(4)
        b = np.array([1,2,3,4])
        _, q = smoothstep_trajectory(a,b)
        np.testing.assert_allclose(q[0],a)
        np.testing.assert_allclose(q[-1],b)

    def test_no_dock(self):
        self.assertEqual(simulate_swap(docked=False),[State.WAIT_FOR_DOCK])

if __name__ == "__main__":
    unittest.main()
