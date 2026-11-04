# Master Research Plan — UAV Battery Swapping and Charging

## 1. Research context
UAV operational endurance is constrained by onboard energy. Autonomous battery exchange aims to reduce service downtime relative to waiting for onboard charging, but introduces difficult mechanical alignment, power safety, state verification, and unattended reliability challenges.

The 2025 university proof-of-concept demonstrated the principle with a 2-DOF arm, magnetic handling and replica batteries. Its reported 12/20 success rate motivates a systematic investigation of alignment, gripper retention, robust control and integration. Those outcomes are historical, not new simulation results.

## 2. Overall aim
Develop and validate a modular, reproducible and safe UAV battery-exchange station with a path toward automatic recharge of removed batteries.

## 3. Research objectives
O1: Formalize functional and quantitative requirements and define target UAV/battery interface.
O2: Compare docking, manipulation and storage architectures using traceable trade studies.
O3: Develop a dimensionally consistent CAD and digital kinematic/dynamic model.
O4: Design mechanical alignment, battery retention, electrical connection and interlocks.
O5: Develop fault-aware supervisory control and sensing interfaces.
O6: Implement simulated scenarios and verify them with automated tests.
O7: Fabricate inert-battery demonstrator and characterize repeatability.
O8: Integrate charging with qualified BMS and protective electrical design.
O9: Quantify reliability, timing, alignment sensitivity, energy and operational cost.
O10: Release reproducible code, datasets, technical reports and publications.

## 4. Testable hypotheses
H1: Constrained docking geometry reduces end-effector positioning error versus an unconstrained landing condition.
H2: Positive battery retention and verified seating improve successful exchange rate relative to the 2025 baseline.
H3: Joint limits and collision-aware trajectory planning reduce aborted exchanges.
H4: Sensor-confirmed state transitions reduce unsafe or incomplete battery transfers.
H5: Parallel charging and inventory scheduling improve station availability versus sequential service.

These hypotheses remain untested for the new design.

## 5. Scope
In scope: single multirotor platform initially; grounded swap station; cold swap first; interchangeable battery cartridge; modular robotic manipulation; charger concept; safety and validation. Future expansion: multi-UAV support, outdoor exposure, fleet scheduling, and commercialization.

Out of scope until formally approved: energized battery experiments without electrical safety review, unsupervised flight testing, hot-swapping flight electronics, and field claims unsupported by data.

## 6. Methods
A. Structured literature review and evidence matrix.
B. Requirements engineering and architecture trade studies.
C. Mechanical design with tolerance stack-up, actuator torque estimates and load cases.
D. Python/MATLAB forward/inverse kinematics and trajectories; CAD motion verification.
E. Sensor and controller state-machine implementation with fault injection.
F. Benchtop experiments with inert replicas, then gated electrical integration.
G. Statistical analysis of repeated trials and sensitivity to landing offset.
H. Reproducible dissemination with versioned code and experiment manifests.

## 7. Measurement plan
Primary: swap success rate, end-to-end time, alignment offset, insertion force, repeatability, unsafe transition count, and failure category.
Secondary: power consumption, charge throughput, inventory availability, cost, maintenance time and weather sensitivity.
Record failed attempts and censored durations explicitly. Report sample size and uncertainty.

## 8. Research integrity
Keep raw data immutable; retain provenance and calibration notes. Cite the 2025 report as the baseline and distinguish new contributions. Do not conflate replica-battery trials with live charging or real-drone tests.

## 9. Gated maturity
G0: evidence and requirements reviewed.
G1: subsystem architecture and interfaces approved.
G2: software tests and CAD motion model validated.
G3: inert-battery bench tests meet agreed acceptance criteria.
G4: electrical protection and charger safety review passed.
G5: integrated UAV tests under controlled conditions.
G6: repeatable demonstration and publication package.

Gates are conditions, not dates or claims of completion.
