"""Metrics for separating simulation and historical trial results."""
from collections import Counter

def summarize_trials(trials: list[dict]) -> dict:
    if not trials:
        return {"attempts": 0, "success_rate": 0.0}
    successes = sum(bool(t.get("success")) for t in trials)
    return {"attempts": len(trials), "successes": successes, "success_rate": successes / len(trials), "failures_by_category": dict(Counter(t.get("failure_category", "unknown") for t in trials if not t.get("success")))}
