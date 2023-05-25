from fastapi import APIRouter


from .motors.router import router as motors_router

router = APIRouter()

router.include_router(motors_router, prefix="/motors", tags=["motors", "devices"])

