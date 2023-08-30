import logging

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from project.app.src.app_info.router import router as app_info
from project.app.src.asset_group.router import router as asset_groups_router
from project.app.src.responsibles.router import router as responsibles_router
from project.app.src.storages.router import router as storages_router
from project.app.src.workplaces.router import router as workplaces_router
from project.app.src.main_services.router import router as main_services_router
from project.app.src.storage_services.router import router as storage_services_router
from project.app.src.suppliers.router import router as suppliers_router
from project.app.src.database import init_db

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
	application = FastAPI(
		title="Warehouse Management",
		description="Welcome to Warehouse Management's API documentation!",
		redoc_url=None,
	)
	application.include_router(app_info)
	application.include_router(asset_groups_router)
	application.include_router(responsibles_router)
	application.include_router(storages_router)
	application.include_router(workplaces_router)
	application.include_router(main_services_router)
	application.include_router(storage_services_router)
	application.include_router(suppliers_router)

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


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
	return JSONResponse(
		status_code=exc.status_code,
		content={"detail": exc.detail},
	)


