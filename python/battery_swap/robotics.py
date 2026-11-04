"""Safety checks shared by motion planners and hardware adapters."""
import numpy as np

def validate_joint_limits(q, limits):
    values = np.asarray(q, dtype=float)
    if values.shape != (len(limits),):
        raise ValueError("joint vector has incorrect dimension")
    if any(not (lo <= value <= hi) for value, (lo, hi) in zip(values, limits)):
        raise ValueError("joint limit violation")
    return True

def check_workspace_distance(point, obstacles, clearance_m=0.0):
    point = np.asarray(point, dtype=float)
    return all(np.linalg.norm(point - np.asarray(center)) >= radius + clearance_m for center, radius in obstacles)
