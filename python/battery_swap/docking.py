from dataclasses import dataclass

@dataclass(frozen=True)
class DockingTolerance:
    position_m: float = .02
    orientation_rad: float = .1

@dataclass(frozen=True)
class DockingMeasurement:
    position_error_m: float
    orientation_error_rad: float
    detected: bool = True
    landed: bool = True

def verify_docking(measurement: DockingMeasurement, tolerance: DockingTolerance = DockingTolerance()) -> tuple[bool, str]:
    if not measurement.detected or not measurement.landed:
        return False, "UAV not detected and landed"
    if measurement.position_error_m > tolerance.position_m:
        return False, "docking position tolerance exceeded"
    if measurement.orientation_error_rad > tolerance.orientation_rad:
        return False, "docking orientation tolerance exceeded"
    return True, "docking verified"
