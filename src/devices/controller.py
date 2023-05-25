from src.devices.device import Device

from src.local_types import Status

class Controller:
    def __init__(self) -> None:
        self.devices: dict[str, Device] = {}
        

    def initialize(self) -> None:
        for device in self.devices.values():
            device.initialize()
    
    
    def get_status(self) -> dict[str, Status]:
        return {name: device.status for name, device in self.devices.items()}
        
            
            
    def add(self, name: str, device: Device) -> None:
        self.devices[name] = device