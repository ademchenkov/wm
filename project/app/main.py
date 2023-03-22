from fastapi import FastAPI

from .routers import info, assets


def create_application() -> FastAPI:
	application = FastAPI()
	application.include_router(info.router)
	application.include_router(assets.router)

	return application


app = create_application()

