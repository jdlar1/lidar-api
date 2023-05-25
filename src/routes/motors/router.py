from fastapi import APIRouter


from src.devices.motors import Motors
from src.settings import settings

router = APIRouter()

motors = Motors()


@router.get("/initialize")
async def initialize():
    motors.initialize(settings.motors_port)
    return {"message": "Motors initialized"}


@router.get("/send/{data}")
async def send(data: str):
    motors.send_str(data)
    response = motors.receive_lines_str(wait = 0.5)
    return {"message": response}


@router.get("/step/{steps}")
async def step(steps: int):
    # has to check it has no more than 6 digits and pad with 0s
    motors.send_str(f"AApdu035{steps:06d}")
    motors.receive_lines_str(wait = 15)

    return {"message": "Motors stepped"}

    