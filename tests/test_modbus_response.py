import threading
import unittest
from unittest.mock import patch

from elegripper_modbus import Gripper


class FakeSerial:
    def __init__(self, response):
        self.response = response
        self.written = b""

    def write(self, data):
        self.written = data

    def flush(self):
        pass

    def read(self, size):
        return self.response[:size]


class ModbusReadResponseTests(unittest.TestCase):
    def test_read_response_uses_six_data_bytes_before_crc(self):
        gripper = object.__new__(Gripper)
        gripper.lock = threading.Lock()
        gripper.cmd_list = [0x0E, 0x03, 0x00, 0x01, 0x00, 0x00]
        gripper.ser = FakeSerial(bytes.fromhex("0e030001000e9531"))

        with patch("elegripper_modbus.time.sleep"):
            result = gripper._Gripper__send_cmd(bytes.fromhex("0e0300010000"))

        self.assertEqual(result, 14)
        self.assertEqual(gripper.ser.written, bytes.fromhex("0e030001000014f5"))


if __name__ == "__main__":
    unittest.main()
