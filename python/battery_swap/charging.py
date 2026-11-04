from enum import Enum
from dataclasses import dataclass

class ChargingState(str, Enum):
    EMPTY="EMPTY"; BATTERY_PRESENT="BATTERY_PRESENT"; AWAITING_INSPECTION="AWAITING_INSPECTION"; READY_TO_CHARGE="READY_TO_CHARGE"; CHARGING="CHARGING"; CHARGE_COMPLETE="CHARGE_COMPLETE"; AVAILABLE="AVAILABLE"; FAULT="FAULT"; ISOLATED="ISOLATED"

@dataclass
class ChargerSlot:
    slot: int
    state: ChargingState = ChargingState.EMPTY
    battery_id: str | None = None
    ready_at_s: float | None = None

    def start(self, battery_id: str, now_s: float, duration_s: float = 3600) -> None:
        if self.state not in (ChargingState.EMPTY, ChargingState.CHARGE_COMPLETE):
            raise RuntimeError("charger slot is not available")
        self.battery_id, self.state, self.ready_at_s = battery_id, ChargingState.CHARGING, now_s + duration_s

    def update(self, now_s: float) -> None:
        if self.state == ChargingState.CHARGING and self.ready_at_s is not None and now_s >= self.ready_at_s:
            self.state = ChargingState.AVAILABLE
