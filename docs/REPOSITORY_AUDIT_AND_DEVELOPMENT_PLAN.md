# Repository Audit and Integrated Development Plan

Status: **In development** (simulation verified for the first integrated slice)

## A. Existing-code audit

| Area | Current state | Evidence | Gap / technical debt |
|---|---|---|---|
| Kinematics | Implemented illustrative 4R forward kinematics | `python/battery_swap/kinematics.py` and unit tests | No inverse kinematics, limits, collision model, or validated CAD dimensions |
| Trajectory | Implemented smoothstep joint interpolation | `trajectory.py` and unit tests | No velocity/acceleration constraint enforcement |
| Swap sequence | Implemented as prerequisite-checked state list | `swap_sequence.py` | Not a supervisory state machine; no subsystem acknowledgements, timeout, recovery, or telemetry |
| Historical analysis | Implemented baseline CSV tests and example | `experiments/baseline_2025`, `tests/test_baseline.py` | Historical evidence must remain separated from simulation results |
| Research/system docs | Present and useful | `research/`, `systems/`, `safety/` | Traceability and verification need linking to executable scenarios |
| Integrated simulation | Added in this delivery | `integrated_simulation.py`, `examples/integrated_swap.py` | Deterministic mock only; no animation, faults beyond initial gates, or hardware I/O |

The repository contains no native CAD, live UAV, charger, or physical validation implementation. Those remain explicitly planned.

## B. Architecture

```text
Simulated UAV ---> Docking verification ---> StationSupervisor ---> Robot model
      |                    |                       |                  |
      +-------------- safety interlock <-----------+                  |
                                                   v                  |
                                      Inventory / charging model      |
                                                   |                  |
                                                   v                  |
                                             Telemetry (JSON records)
```

The supervisor owns workflow transitions. Subsystems report state; issuing a command is not completion. The current slice uses synchronous mock acknowledgements so the contract can be tested before asynchronous adapters are introduced.

## C. Initial requirements traceability

| Requirement | Module | Verification |
|---|---|---|
| Reject misaligned UAV | `integrated_simulation.py` | `test_bad_docking_aborts_safely` |
| Require propulsion inhibition | `integrated_simulation.py` | Add armed-UAV scenario in Phase B |
| Require compatible charged battery | `Inventory.select_charged` | `test_no_charged_battery_aborts_safely` |
| Complete end-to-end exchange | `StationSupervisor.run_swap` | `test_successful_end_to_end_swap` |
| Record meaningful events | `Telemetry` | Successful test checks `swap_completed`; expand schema tests in Phase B |
| Preserve historical baseline | baseline CSV and tests | `tests/test_baseline.py` |

## D. Prioritized backlog

1. **B1 — Formal supervisor state machine** (3–5 days). Dependency: current integrated slice. Acceptance: explicit transitions, timeout policy, fault and recovery tests for all 15 required scenarios.
2. **B2 — Configuration schemas** (2–3 days). Dependency: robot/docking/battery parameter decisions. Acceptance: YAML validation, SI units, invalid-config rejection.
3. **B3 — Robot safety model** (4–6 days). Dependency: B2. Acceptance: joint limits, reachability, trajectory limits, collision checks and tests.
4. **B4 — Docking/localization interfaces** (3–5 days). Dependency: B2. Acceptance: configurable tolerances, simulated sensor disagreement and pose error logs.
5. **B5 — Battery storage and charging state model** (4–6 days). Dependency: B2. Acceptance: reservations, conflicts, charging faults, readiness estimates.
6. **B6 — Structured telemetry and experiment runner** (3–5 days). Dependency: B1–B5. Acceptance: JSONL replay, deterministic seeds, metrics report.
7. **C1 — Digital-twin visualization** (5–8 days). Dependency: B3/B4/B5. Acceptance: visual state derives from simulation state; configurable offsets and slots.
8. **D1 — Hardware adapter contracts and HIL plan** (5–8 days). Dependency: B1/B4/B5. Acceptance: mocks run without supervisor changes; safety review gates documented.

## E. First integrated simulation

Run from the repository root:

```text
python -m unittest discover -s tests -v
python examples/integrated_swap.py
```

The normal path verifies docking, propulsion inhibition, inventory selection, storage reservation, insertion, final connection verification, and completion. Failure paths transition to `SAFE_ABORT` and record the reason.

## F. Verification report

The implementation is simulation-only and uses illustrative dimensions and mocked subsystem acknowledgements. It does not claim charging hardware, UAV autopilot integration, CAD integration, force sensing, or experimental performance. Historical 2025 results remain measured historical evidence and are not mixed with new simulation results.

Known limitations: no asynchronous timeouts, inverse kinematics, collision detection, charger state machine, JSONL persistence, animation, or hardware-rated interlocks. These are tracked in the backlog above.
