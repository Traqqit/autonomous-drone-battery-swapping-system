"""Illustrative supervisory states, not a hardware controller."""
from enum import Enum, auto

class State(Enum):
    WAIT_FOR_DOCK = auto()
    ALIGN = auto()
    GRIP_SPENT = auto()
    REMOVE_SPENT = auto()
    STORE_SPENT = auto()
    GRIP_CHARGED = auto()
    INSERT_CHARGED = auto()
    RELEASE = auto()
    VERIFY = auto()
    COMPLETE = auto()

SEQUENCE = tuple(State)

def simulate_swap(docked=True, charged_battery_available=True, verified=True):
    """Return planned states; refuse progression if prerequisites fail."""
    if not docked:
        return [State.WAIT_FOR_DOCK]
    if not charged_battery_available:
        raise RuntimeError("No charged battery available")
    if not verified:
        raise RuntimeError("Battery engagement verification failed")
    return list(SEQUENCE)
