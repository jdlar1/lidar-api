from fastapi import APIRouter

from src.controller import controller

router = APIRouter()

@router.get("/initialize")
async def initialize():
    controller.devices["motors"].initialize()
    return {"message": "Motors initialized"}


@router.get("/send/{data}")
async def send(data: str):
    controller.devices["motors"].send_str(data) # type: ignore
    response = controller.devices["motors"].receive_lines_str(wait = 0.5) # type: ignore
    return {"message": response}


@router.get("/step/{steps}")
async def step(steps: int):
    # has to check it has no more than 6 digits and pad with 0s
    controller.devices["motors"].send_str(f"AApdu035{steps:06d}") # type: ignore
    controller.devices["motors"].receive_lines_str(wait = 15) # type: ignore

    return {"message": "Motors stepped"}

    