from dataclasses import dataclass

@dataclass
class SafetyInterlocks:
    emergency_stop: bool = False
    motors_armed: bool = False
    sensor_disagreement: bool = False
    communication_ok: bool = True

    def permits_robot_motion(self) -> bool:
        return not (self.emergency_stop or self.motors_armed or self.sensor_disagreement or not self.communication_ok)

    def require_motion_permit(self) -> None:
        if not self.permits_robot_motion():
            raise RuntimeError("safety interlock prevents robot motion")
