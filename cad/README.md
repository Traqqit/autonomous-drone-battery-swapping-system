# CAD — proposed advanced arm

The supplied reference image depicts a white/black articulated arm with a
dark mounting plate, cylindrical base, rounded links, circular joint housings,
orange tool mount and parallel-jaw gripper. It is a **visual reference only**.

Proposed kinematic chain:
- J1 base yaw: full rotation in the kinematic model
- J2 shoulder pitch
- J3 elbow pitch
- J4 wrist pitch
- G1 symmetric parallel-jaw opening

**Illustrative model dimensions, not measured from the image:**
upper 285 mm, forearm 250 mm, tool 95 mm, shoulder height 300 mm.

**Historical 2025 prototype (different mechanism):**
upper arm 120 mm, forearm 90 mm (Table 3.2 of university report).

Future CAD deliverables:
`Base.SLDPRT`, `Waist.SLDPRT`, `Shoulder.SLDPRT`,
`UpperArm.SLDPRT`, `Forearm.SLDPRT`, `Wrist.SLDPRT`,
`Gripper.SLDPRT`, `LeftJaw.SLDPRT`, `RightJaw.SLDPRT`,
and `RobotArm.SLDASM`. These files are NOT yet generated.

Import into Autodesk Inventor may preserve geometry but does not guarantee
transfer of native SolidWorks mates. Verify/recreate motion joints in Inventor.
Continuous base rotation in hardware requires a designed cable/actuator solution.
