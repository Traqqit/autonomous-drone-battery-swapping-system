"""Simple 4R arm model. Angles in radians; lengths in metres."""
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class Arm:
    shoulder_height: float = 0.30
    upper: float = 0.285
    forearm: float = 0.250
    tool: float = 0.095

    def points(self, q):
        """Return (5,3) points: base, shoulder, elbow, wrist, tool tip."""
        q = np.asarray(q, dtype=float)
        if q.shape != (4,):
            raise ValueError("Expected [base, shoulder, elbow, wrist] in radians")
        yaw, shoulder, elbow, wrist = q
        pitch = np.cumsum([shoulder, elbow, wrist])
        lengths = [self.upper, self.forearm, self.tool]
        radii = np.cumsum([0.0] + [l * np.cos(a) for l, a in zip(lengths, pitch)])
        heights = self.shoulder_height + np.cumsum(
            [0.0] + [l * np.sin(a) for l, a in zip(lengths, pitch)]
        )
        points = [[0.0, 0.0, 0.0]]
        points += [[r*np.cos(yaw), r*np.sin(yaw), z]
                   for r,z in zip(radii, heights)]
        return np.array(points, dtype=float)

    def tool_position(self, q):
        return self.points(q)[-1]
