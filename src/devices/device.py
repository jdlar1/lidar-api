from abc import ABC, abstractmethod


from src.local_types import Status

class Device(ABC):
    @abstractmethod
    def initialize() -> bool:
        ...
        

    @property
    @abstractmethod
    def status(self) -> Status:
        ...