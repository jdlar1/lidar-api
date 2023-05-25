from src.devices.motors import Motors
from src.devices.controller import Controller

from .settings import settings

controller = Controller()

controller.add("motors", Motors(settings.motors_port))

