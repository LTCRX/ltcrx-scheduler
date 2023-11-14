from fastapi import FastAPI
from mangum import Mangum
from sqlalchemy_utils import database_exists, create_database
from fastapi.middleware.cors import CORSMiddleware

from core.configs.settings import settings
from infrastructure.api.v1 import router as api_router
from infrastructure.persistence.repository.session import engine


def create_database_if_not_exists():
    if not database_exists(engine.url):
        create_database(engine.url)


def start_application():
    app = FastAPI(
        title=settings.PROJECT_TITLE,
        varion=settings.PROJECT_VERSION,
        root_path=settings.ROOT_PATH,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    create_database_if_not_exists()
    app.include_router(api_router, prefix="/api/v1")
    return app


app = start_application()

# to make it work with Amazon Lambda, we create a handler object
handler = Mangum(app=app)
