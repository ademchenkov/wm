import logging

from fastapi import FastAPI

from .databases.postgres import init_db
from .api import InfoApi, AssetGroupApi

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
	application = FastAPI()
	application.include_router(AssetGroupApi.router)
	application.include_router(InfoApi.router)

	return application


app = create_application()


@app.on_event("startup")
async def startup_event():
	logging.info("Starting up...")
	await init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
	logging.info("Shutting down...")
