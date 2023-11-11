from fastapi import APIRouter


router = APIRouter()


@router.get("/dummy")
def dummy():
    return {"response": "scheduller dummy endpoint"}
