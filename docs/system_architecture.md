# Architecture

Historical demonstration:
drone replica → V-shaped landing guide + ultrasonic detection → Arduino →
two-servo arm + magnetic claw ↔ two-position rotating battery platter.

Proposed system:
docking sensor → supervisory state machine → joint planner → arm actuators →
battery gripper; with battery presence, latch state, and fault handling.

No live battery charging is implemented. Physical hardware integration requires
electrical protection, battery management, verified interlocks and a safety review.
