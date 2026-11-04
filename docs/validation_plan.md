# Validation protocol (proposed, not yet performed)

Record one row per trial: timestamp, build revision, battery dummy mass, docking
offset, success, swap duration, failure category, and operator observations.

Predefine success as: battery removed, stored, replacement inserted and seated,
gripper released, arm returned home, no interlock fault.

Analyze success rate with uncertainty; report successful-trial swap time separately
from all-attempt time; preserve failures as failures, not zero-second swaps.
Use multiple repetitions at different imposed alignment offsets.

Physical tests should begin with inert battery replicas and a mechanically
constrained fixture before introducing energized battery packs.
