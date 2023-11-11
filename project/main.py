from fastapi import FastAPI
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware

from core.configs.settings import settings
from infrastructure.api.v1 import router as api_router


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
    app.include_router(api_router, prefix="/api/v1")
    return app


app = start_application()

# to make it work with Amazon Lambda, we create a handler object
handler = Mangum(app=app)
