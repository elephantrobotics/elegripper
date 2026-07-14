# Elephant Gripper Python Library

This Python library controls an Elephant Robotics gripper over a serial port.
`elegripper_modbus.py` uses Modbus RTU framing.

## Installation

```bash
pip install pyserial
```

## Quick start

```python
from elegripper_modbus import Gripper

gripper = Gripper("COM3", baudrate=115200, id=14)
try:
    gripper.set_gripper_enable(1)
    gripper.set_gripper_value(50, speed=80)
    print(gripper.get_gripper_value())
finally:
    gripper.ser.close()
```

On Linux, replace `COM3` with the device path, such as `/dev/ttyUSB0`.

## Return values and communication errors

Most methods return the integer value from the device. The communication layer
can also return or raise:

- `-1`: response length is invalid.
- `-2`: Modbus CRC validation failed.
- `TimeoutError`: serial read timed out.

Function 03 responses from this device are eight bytes: six data bytes followed
by two CRC bytes. For example, request `0e030001000014f5` can receive
`0e030001000e9531`.

## Query methods

| Method | Return value |
| --- | --- |
| `get_firmware_version()` | Firmware major version |
| `get_modified_version()` | Firmware minor version |
| `get_gripper_Id()` | Gripper ID |
| `get_gripper_baud()` | Baud-rate index (0–5) |
| `get_gripper_value()` | Current position (0–100) |
| `get_gripper_status()` | 0=moving; 1=stopped without an object; 2=stopped with an object; 3=object fell after detection |
| `get_gripper_speed()` | Current speed (1–100) |
| `get_gripper_P()` | PID P value (0–254) |
| `get_gripper_I()` | PID I value (0–254) |
| `get_gripper_D()` | PID D value (0–254) |
| `get_gripper_cw()` | Clockwise run error (0–16) |
| `get_gripper_cww()` | Counter-clockwise run error (0–16) |
| `get_gripper_mini_pressure()` | Minimum starting pressure (0–254) |
| `get_gripper_torque()` | Gripper torque (0–300) |
| `get_gripper_io_open_value()` | IO open position (0–100) |
| `get_gripper_io_close_value()` | IO close position (0–100) |
| `get_gripper_queue_count()` | Number of queued commands |
| `get_gripper_vir_pos()` | Virtual position (0–100) |
| `get_gripper_protection_current()` | Protection current |

## Configuration and motion methods

| Method | Parameters and behavior |
| --- | --- |
| `set_gripper_Id(value)` | ID, `1–254` |
| `set_gripper_baud(value=0)` | Baud-rate index: 0=115200, 1=1000000, 2=57600, 3=19200, 4=9600, 5=4800 |
| `set_gripper_enable(value)` | Enable state: 0=disabled, 1=enabled |
| `set_gripper_value(value, speed=100)` | Position `0–100`; speed `1–100` |
| `set_gripper_speed(value)` | Speed `0–100` |
| `set_gripper_calibration()` | Run zero-position calibration |
| `set_gripper_P(value)` | PID P value, `0–254` |
| `set_gripper_I(value)` | PID I value, `0–254` |
| `set_gripper_D(value)` | PID D value, `0–254` |
| `set_gripper_cw(value)` | Clockwise run error, `0–16` |
| `set_gripper_cww(value)` | Counter-clockwise run error, `0–16` |
| `set_gripper_mini_pressure(value)` | Minimum starting pressure, `0–254` |
| `set_gripper_torque(value)` | Gripper torque, `0–100` |
| `set_gripper_output(value=0)` | IO output: 0=all off, 1=OUT1 on, 2=OUT2 on, 3=all on |
| `set_gripper_io_open_value(value)` | IO open position, `0–100` |
| `set_gripper_io_close_value(value)` | IO close position, `0–100` |
| `set_abs_gripper_value(value, speed=100)` | Absolute position `0–100`; speed `1–100` |
| `set_gripper_pause()` | Pause absolute-position movement |
| `set_gripper_resume()` | Resume absolute-position movement |
| `set_gripper_stop()` | Stop movement and clear the command cache |
| `set_gripper_vir_pos(value)` | Set virtual position, `0–100` |
| `set_gripper_protection_current(value)` | Set protection current, `100–300` |
| `set_gripper_state(value, speed=100)` | 0=fully closed, 1=fully open; speed `1–100` |

## Example

Run the included example:

```bash
python demo.py
```
