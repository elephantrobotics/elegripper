# Elephant Gripper Python 库

通过串口控制 Elephant Robotics 夹爪的 Python 接口。`elegripper_modbus.py`
使用 Modbus RTU 帧格式。

## 安装

```bash
pip install pyserial
```

## 快速开始

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

Linux 请将 `COM3` 替换为对应设备路径，例如 `/dev/ttyUSB0`。

## 返回值与通信错误

多数接口返回设备回传的整数值。通信层还会返回或抛出以下结果：

- `-1`：收到的响应长度不正确。
- `-2`：Modbus CRC 校验失败。
- `TimeoutError`：串口读取超时。

Function 03 的本设备响应为 8 字节：6 字节数据和 2 字节 CRC。例如请求
`0e030001000014f5` 的响应可为 `0e030001000e9531`。

## 查询接口

| 接口 | 返回值 |
| --- | --- |
| `get_firmware_version()` | 固件主版本号 |
| `get_modified_version()` | 固件次版本号 |
| `get_gripper_Id()` | 夹爪 ID |
| `get_gripper_baud()` | 波特率索引（0–5） |
| `get_gripper_value()` | 当前开合位置（0–100） |
| `get_gripper_status()` | 状态：0 运动中；1 停止未夹到物体；2 已夹到物体；3 夹取后物体掉落 |
| `get_gripper_speed()` | 当前速度（1–100） |
| `get_gripper_P()` | PID P 值（0–254） |
| `get_gripper_I()` | PID I 值（0–254） |
| `get_gripper_D()` | PID D 值（0–254） |
| `get_gripper_cw()` | 顺时针运行误差（0–16） |
| `get_gripper_cww()` | 逆时针运行误差（0–16） |
| `get_gripper_mini_pressure()` | 最小启动压力（0–254） |
| `get_gripper_torque()` | 夹爪扭矩（0–300） |
| `get_gripper_io_open_value()` | IO 打开位置（0–100） |
| `get_gripper_io_close_value()` | IO 关闭位置（0–100） |
| `get_gripper_queue_count()` | 当前命令队列数量 |
| `get_gripper_vir_pos()` | 虚拟位置（0–100） |
| `get_gripper_protection_current()` | 保护电流 |

## 配置与运动接口

| 接口 | 参数与说明 |
| --- | --- |
| `set_gripper_Id(value)` | ID，`1–254` |
| `set_gripper_baud(value=0)` | 波特率索引：0=115200、1=1000000、2=57600、3=19200、4=9600、5=4800 |
| `set_gripper_enable(value)` | 使能：0 禁用，1 启用 |
| `set_gripper_value(value, speed=100)` | 目标开合位置 `0–100`；速度 `1–100` |
| `set_gripper_speed(value)` | 速度 `0–100` |
| `set_gripper_calibration()` | 执行零位校准 |
| `set_gripper_P(value)` | PID P 值，`0–254` |
| `set_gripper_I(value)` | PID I 值，`0–254` |
| `set_gripper_D(value)` | PID D 值，`0–254` |
| `set_gripper_cw(value)` | 顺时针运行误差，`0–16` |
| `set_gripper_cww(value)` | 逆时针运行误差，`0–16` |
| `set_gripper_mini_pressure(value)` | 最小启动压力，`0–254` |
| `set_gripper_torque(value)` | 夹爪扭矩，`0–100` |
| `set_gripper_output(value=0)` | IO 输出：0=全关、1=OUT1 开、2=OUT2 开、3=全开 |
| `set_gripper_io_open_value(value)` | IO 打开位置，`0–100` |
| `set_gripper_io_close_value(value)` | IO 关闭位置，`0–100` |
| `set_abs_gripper_value(value, speed=100)` | 绝对位置 `0–100`；速度 `1–100` |
| `set_gripper_pause()` | 暂停绝对位置运动 |
| `set_gripper_resume()` | 恢复绝对位置运动 |
| `set_gripper_stop()` | 停止运动并清空命令缓存 |
| `set_gripper_vir_pos(value)` | 设置虚拟位置，`0–100` |
| `set_gripper_protection_current(value)` | 设置保护电流，`100–300` |
| `set_gripper_state(value, speed=100)` | 0 全闭合，1 全打开；速度 `1–100` |

## 示例

运行仓库中的示例：

```bash
python demo.py
```
