import time
from serial import Serial


from .device import Device


class Motors(Device):
    def __init__(self, port: str, baudrate: int = 9600):
        self.port = port
        self.baudrate = baudrate
        self.serial = Serial(port, baudrate)

    def initialize(self) -> bool:
        self.serial.open()
        time.sleep(2)

        self.send_str("CONF")
        lines = self.receive_lines_str()

        return len(lines[0]) > 0
        

    def teardown(self) -> None:
        self.serial.close()

    def send_str(self, data: str) -> None:
        binary_data = data.encode() + b"\r\n"
        self.serial.write(binary_data)

    def receive_lines_str(self, wait: float = 0.1) -> list[str]:
        time.sleep(wait)
        lines = self.serial.readlines()
        return [line.decode() for line in lines]

    def __repr__(self) -> str:
        return f"Motor(port={self.port}, baudrate={self.baudrate})"
