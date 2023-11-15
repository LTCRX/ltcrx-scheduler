from fastapi import APIRouter, Depends

from core.domain.user import User
from infrastructure.api.v1.controller.dependencies.token import get_user_by_token

router = APIRouter()


@router.get("/dummy")
def dummy(current_user: User = Depends(get_user_by_token)):
    return {"response": f"scheduller dummy endpoint, current_user={current_user.username}"}
