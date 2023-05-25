from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def initialize() -> bool:
        ...