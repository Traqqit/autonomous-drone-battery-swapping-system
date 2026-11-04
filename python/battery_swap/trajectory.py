"""Time-parametrized smooth joint-space interpolation."""
import numpy as np

def smoothstep_trajectory(q_start, q_end, duration=3.0, samples=100):
    if duration <= 0 or samples < 2:
        raise ValueError("duration must be positive and samples >= 2")
    a, b = np.asarray(q_start, dtype=float), np.asarray(q_end, dtype=float)
    if a.shape != (4,) or b.shape != (4,):
        raise ValueError("Both joint vectors must contain four angles")
    t = np.linspace(0, duration, samples)
    s = t / duration
    blend = 3*s*s - 2*s*s*s
    return t, a[None,:] + blend[:,None] * (b-a)[None,:]
