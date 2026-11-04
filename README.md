# Autonomous UAV Battery Swapping and Charging — Full Research Program
**Collaborative ongoing research:** Irungu Josphat Macharia and Israel Nyakoe Maragia  
**Repository owner (proposed):** [Traqqit](https://github.com/Traqqit)  
**Research stage:** Historical proof-of-concept + computational baseline; integrated next-generation system is planned, not yet validated.

## Mission
Design, simulate, fabricate, integrate and experimentally validate an autonomous UAV battery exchange and charging station that improves docking tolerance, reliability, cycle time, safety and maintainability.

## Evidence boundaries
**Demonstrated in the 2025 university report:** 2-DOF Arduino-controlled prototype, magnetic battery handling, battery carousel, replica drone/batteries, 20 trials, 12 successes (60%), approximately 90 seconds per successful swap. No live charging or real drone tests.

**Currently runnable in this repository:** illustrative 4R forward kinematics, joint interpolation, sequence logic, workspace sampling, baseline trial analysis, Python tests and MATLAB demonstration.

**Planned, not completed:** physical 4R robot, gripper, full SolidWorks/Inventor assembly, perception, flight-controller interface, electrical charging hardware, digital twin, integration tests and field trials.

## Research work packages
| ID | Package | Outputs |
|---|---|---|
| WP01 | Research and literature | structured review, gap analysis, hypotheses |
| WP02 | Requirements and system engineering | requirements, interfaces, traceability, trade studies |
| WP03 | UAV and battery interface | drone envelope, battery cartridge, access and connector specification |
| WP04 | Docking and localization | landing fixture, pose sensing, alignment error budget |
| WP05 | Manipulator and gripper | CAD, kinematics, dynamics, motion and force constraints |
| WP06 | Storage and charging | inventory logic, charging architecture, BMS and interlocks |
| WP07 | Electronics and embedded | schematics, power distribution, firmware and sensors |
| WP08 | Autonomy and software | state machine, flight/ground interface, recovery, logs |
| WP09 | Simulation and digital twin | coupled mechanical/control simulation, scenarios |
| WP10 | Safety, risk and reliability | hazard log, FMEA, safe-state validation |
| WP11 | Experiments and statistics | protocols, raw datasets, repeatability, KPIs |
| WP12 | Manufacturing, economics and publication | BOM, assembly, costing, reproducibility, papers |

## Start here
1. Read `research/MASTER_RESEARCH_PLAN.md` and `systems/requirements.csv`.
2. Agree on one target UAV and battery cartridge before committing to dimensions.
3. Run `python -m pip install -r requirements.txt`.
4. Run `python -m unittest discover -s tests -v`.
5. Run `python examples/demo.py`, `python examples/analyze_baseline.py`, and `python examples/workspace_sample.py`.
6. Open GitHub issues from `research/WORK_PACKAGES.md` and assign package leads.
7. Capture all test evidence using `experiments/TEMPLATE.md`.
8. Run the first integrated simulation with `python examples/integrated_swap.py` and read `docs/REPOSITORY_AUDIT_AND_DEVELOPMENT_PLAN.md`.

## Repository conventions
Every research claim must be labeled **historical measured**, **new measured**, **simulation**, **assumption**, or **target**. Every subsystem must trace to a requirement and verification method. Avoid publishing full university report or third-party CAD until permissions are confirmed. Licensing is pending joint agreement.

See `ROADMAP.md`, `CONTRIBUTING.md`, `AUTHORS.md`, `research/`, `systems/`, `safety/`, and `experiments/`.
