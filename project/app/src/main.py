import logging
from fastapi import FastAPI

from project.app.src.app_status.router import router as app_status_router
from project.app.src.asset_group.router import router as asset_group_router
from project.app.src.database import init_db

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
	application = FastAPI(
		title="Warehouse Management",
		description="Welcome to Warehouse Management's API documentation!",
		#root_path="/api/v1",
		docs_url="/docs",
		#openapi_url="/docs/openapi.json",
		redoc_url=None,
	)
	application.include_router(app_status_router)
	application.include_router(asset_group_router)

	return application


app = create_application()


@app.on_event("startup")
async def startup_event():
	logging.info("Starting up...")
	await init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
	logging.info("Shutting down...")


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
	return {"status": "ok"}
