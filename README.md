# Autonomous Drone Battery Swapping System

**University project companion and proposed robotic-arm simulation**

This repository documents a cold-swapping drone battery prototype described in the
uploaded January 2025 university report, and separately provides an **original
illustrative Python/MATLAB model** for a proposed articulated-arm upgrade.

## Reported university prototype (not reproduced by the simulation)
- Two-degree-of-freedom robotic arm and magnetic claw
- Carousel-like battery holding platter
- Arduino-controlled sequence
- 3D-printed drone and battery replicas
- Reported average swap time: **90 seconds**
- Reported reliability: **60%** in preliminary tests

These are **report-reported measurements**, not results produced by the scripts here.
The original prototype used replica batteries; this repository does not claim live
charging or successful operation on a flight-ready UAV.

## Proposed simulation (separate from the prototype)
A simplified 4-revolute-joint arm: base yaw, shoulder pitch, elbow pitch,
wrist pitch, plus an independently actuated parallel gripper. The planar
arm chain is rotated about the vertical base axis. It is a kinematic
demonstration, **not** a collision-free, torque-validated or hardware-ready robot.

## Quick start (Python 3.10+)
```bash
python -m pip install -r requirements.txt
python examples/demo.py
python -m unittest discover -s tests -v
```
Outputs a plot at `examples/robot_trajectory.png` and prints representative
end-effector positions and swap-state transitions.

## MATLAB
Run `matlab/demo_trajectory.m` from MATLAB. It implements the same joint
convention and sample motion using core MATLAB functions.

## CAD
See `cad/README.md`. Native SolidWorks parts/assembly and verified Inventor
joints are **not included**. The original reference image is not a dimensioned
manufacturing drawing.

## Project status
- [x] Forward kinematics
- [x] Joint interpolation
- [x] Simplified swapping state machine
- [x] Unit tests
- [x] MATLAB kinematic demonstration
- [ ] Verified CAD geometry and Inventor motion joints
- [ ] Measured motor torques, sensor feedback, safety interlocks
- [ ] Validated battery insertion and charging hardware

## Sources and attribution
See `docs/sources.md`. The uploaded university report is a source of project
context, not evidence that these particular scripts were written or used during
the original project. Do not represent generated example scripts as historical
university submissions.

## License
No software license has been selected. Add a LICENSE file only after the
project authors agree on permissions and any third-party assets are reviewed.
