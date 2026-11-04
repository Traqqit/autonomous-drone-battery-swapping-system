"""Run from repository root: python examples/demo.py"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "python"))
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from battery_swap.kinematics import Arm
from battery_swap.trajectory import smoothstep_trajectory
from battery_swap.swap_sequence import simulate_swap

arm = Arm()
q0 = np.deg2rad([0, 25, -55, 20])
q1 = np.deg2rad([120, 50, -85, 15])
t, qs = smoothstep_trajectory(q0, q1, duration=4.0)
xyz = np.array([arm.tool_position(q) for q in qs])
fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111, projection="3d")
ax.plot(xyz[:,0], xyz[:,1], xyz[:,2], label="Tool-tip path")
for q in (q0, q1):
    pts = arm.points(q)
    ax.plot(pts[:,0], pts[:,1], pts[:,2], marker="o")
ax.set(xlabel="X (m)", ylabel="Y (m)", zlabel="Z (m)",
       title="Proposed 4R robotic-arm kinematic demonstration")
ax.legend()
fig.tight_layout()
output = Path(__file__).with_name("robot_trajectory.png")
fig.savefig(output, dpi=160)
print("Saved:", output)
print("Start tool position (m):", arm.tool_position(q0).round(4))
print("End tool position (m):", arm.tool_position(q1).round(4))
print("States:", " -> ".join(s.name for s in simulate_swap()))
