from fastapi import APIRouter

from infrastructure.api.v1.controller import scheduler_controller, user_controller, token_controler

router = APIRouter()

router.include_router(
    scheduler_controller.dummy_controller.router,
    prefix="/dummy",
    tags=["Endpoint to scheduler experiments on LTC-RX"],
)

router.include_router(
    scheduler_controller.scheduler_controller.router,
    prefix="/scheduler",
    tags=["Endpoint to scheduler experiments on LTC-RX"],
)

router.include_router(
    user_controller.user_controller.router,
    prefix="/users",
    tags=["Endpoint to LTC-RX users"],
)

router.include_router(
    token_controler.token_controller.router,
    prefix="/token",
    tags=["Endpoint to LTC-RX users"],
)
