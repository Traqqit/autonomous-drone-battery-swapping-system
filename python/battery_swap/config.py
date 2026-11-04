"""Validated, SI-unit configuration for the simulation."""
from dataclasses import dataclass
from pathlib import Path
import json

@dataclass(frozen=True)
class RobotConfig:
    upper_arm_length_m: float = .285
    forearm_length_m: float = .250
    tool_length_m: float = .095
    joint_limits_rad: tuple[tuple[float, float], ...] = ((-3.14159, 3.14159),) * 4

    def validate(self):
        if min(self.upper_arm_length_m, self.forearm_length_m, self.tool_length_m) <= 0:
            raise ValueError("robot link lengths must be positive")
        if len(self.joint_limits_rad) != 4 or any(lo >= hi for lo, hi in self.joint_limits_rad):
            raise ValueError("four valid joint limits are required")

def load_json(path: str | Path) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("configuration root must be an object")
    return data
