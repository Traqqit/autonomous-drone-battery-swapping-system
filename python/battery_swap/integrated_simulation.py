"""Deterministic, hardware-independent end-to-end swap simulation."""
from dataclasses import dataclass, field
from enum import Enum
from time import time

from .kinematics import Arm


class StationState(str, Enum):
    IDLE = "IDLE"
    WAITING_FOR_UAV = "WAITING_FOR_UAV"
    SAFETY_INTERLOCK_CHECK = "SAFETY_INTERLOCK_CHECK"
    ROBOT_HOMING = "ROBOT_HOMING"
    EXTRACT_DEPLETED_BATTERY = "EXTRACT_DEPLETED_BATTERY"
    STORE_DEPLETED_BATTERY = "STORE_DEPLETED_BATTERY"
    SELECT_CHARGED_BATTERY = "SELECT_CHARGED_BATTERY"
    INSERT_REPLACEMENT = "INSERT_REPLACEMENT"
    FINAL_SYSTEM_CHECK = "FINAL_SYSTEM_CHECK"
    SWAP_COMPLETE = "SWAP_COMPLETE"
    SAFE_ABORT = "SAFE_ABORT"


@dataclass
class SimUAV:
    detected: bool = True
    landed: bool = True
    motors_armed: bool = False
    service_requested: bool = True
    dock_position_error_m: float = 0.002
    dock_orientation_error_rad: float = 0.01
    battery_id: str = "spent-001"
    exchange_complete: bool = False


@dataclass
class Battery:
    battery_id: str
    state_of_charge: float
    compatible: bool = True
    slot: int | None = None
    fault: bool = False

    @property
    def available(self) -> bool:
        return self.compatible and not self.fault and self.state_of_charge >= 0.8


@dataclass
class Inventory:
    batteries: list[Battery]
    reserved_slot: int | None = None

    def select_charged(self) -> Battery | None:
        return next((b for b in self.batteries if b.available and b.slot != self.reserved_slot), None)

    def reserve_empty_slot(self) -> int:
        used = {b.slot for b in self.batteries if b.slot is not None}
        for slot in range(4):
            if slot not in used:
                self.reserved_slot = slot
                return slot
        raise RuntimeError("No empty storage slot")


@dataclass
class Telemetry:
    events: list[dict] = field(default_factory=list)

    def record(self, event: str, state: StationState, **details) -> None:
        self.events.append({"timestamp": time(), "event": event, "state": state.value, **details})


@dataclass
class SwapResult:
    success: bool
    final_state: StationState
    events: list[dict]
    failure: str | None = None


class StationSupervisor:
    """Coordinates mocked subsystems and enforces simulation safety gates."""
    def __init__(self, uav: SimUAV, inventory: Inventory, arm: Arm | None = None):
        self.uav, self.inventory, self.arm = uav, inventory, arm or Arm()
        self.state = StationState.IDLE
        self.telemetry = Telemetry()

    def _enter(self, state: StationState, event: str, **details):
        self.state = state
        self.telemetry.record(event, state, **details)

    def run_swap(self) -> SwapResult:
        try:
            self._enter(StationState.WAITING_FOR_UAV, "service_requested")
            if not (self.uav.detected and self.uav.landed):
                raise RuntimeError("UAV not detected and landed")
            if self.uav.dock_position_error_m > 0.02 or self.uav.dock_orientation_error_rad > 0.1:
                raise RuntimeError("docking tolerance exceeded")
            self._enter(StationState.SAFETY_INTERLOCK_CHECK, "docking_verified")
            if self.uav.motors_armed:
                raise RuntimeError("propulsion is not inhibited")
            spent = next((b for b in self.inventory.batteries if b.battery_id == self.uav.battery_id), None)
            if spent is None:
                raise RuntimeError("UAV battery is not in inventory")
            replacement = self.inventory.select_charged()
            if replacement is None:
                raise RuntimeError("no compatible charged battery available")
            slot = self.inventory.reserve_empty_slot()
            self._enter(StationState.ROBOT_HOMING, "robot_homed")
            self._enter(StationState.EXTRACT_DEPLETED_BATTERY, "battery_gripped", battery_id=spent.battery_id)
            self._enter(StationState.STORE_DEPLETED_BATTERY, "battery_stored", battery_id=spent.battery_id, slot=slot)
            spent.slot, spent.state_of_charge = slot, 0.0
            self._enter(StationState.SELECT_CHARGED_BATTERY, "charged_battery_selected", battery_id=replacement.battery_id)
            self._enter(StationState.INSERT_REPLACEMENT, "battery_inserted", battery_id=replacement.battery_id)
            self._enter(StationState.FINAL_SYSTEM_CHECK, "connection_verified")
            self.uav.battery_id, self.uav.exchange_complete = replacement.battery_id, True
            self._enter(StationState.SWAP_COMPLETE, "swap_completed")
            return SwapResult(True, self.state, self.telemetry.events)
        except RuntimeError as exc:
            self._enter(StationState.SAFE_ABORT, "safe_abort", reason=str(exc))
            return SwapResult(False, self.state, self.telemetry.events, str(exc))
