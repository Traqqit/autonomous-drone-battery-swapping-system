# Integrated System Architecture
UAV requests landing → docking guides and sensors constrain pose → verify landed and disarmed → grip depleted battery → extract → store → select verified charged battery → insert and latch → verify seating → retract arm → release UAV.
The charging subsystem is isolated from robotic motion and operates only after BMS/thermal/electrical safety checks.
Interfaces: UAV-to-station flight status; docking-to-controller pose; robot-to-controller motion state; battery-to-inventory ID; BMS-to-charger charge permission; independent safety interlocks.
Coordinate frames: world W, dock D, robot base B, end-effector T, UAV U and battery cartridge C. Units: SI, CAD drawings in mm.
