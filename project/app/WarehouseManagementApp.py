import os

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from .routers import info, assets


def create_application() -> FastAPI:
	application = FastAPI()
	application.include_router(info.router)
	application.include_router(assets.router)

	return application


app = create_application()

register_tortoise(
	app,
	db_url=os.environ.get("DATABASE_URL"),
	modules={"models": ["project.app.models.tortoise.Asset"]},
	generate_schemas=False,
	add_exception_handlers=True,
)
