from fastapi import APIRouter

from infrastructure.api.v1.controller import scheduler_controller

router = APIRouter()


router.include_router(
    scheduler_controller.dummy_controller.router,
    prefix="/scheduler",
    tags=["Endpoint to scheduler experiments on LTC-RX"],
)
