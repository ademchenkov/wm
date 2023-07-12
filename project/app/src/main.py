import logging

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from tortoise.exceptions import IntegrityError

from project.app.src.app_info.router import router as app_info
from project.app.src.asset_group.router import router as asset_group_router
from project.app.src.responsible.router import router as responsible_router
from project.app.src.storage.router import router as storage_router
from project.app.src.database import init_db

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
	application = FastAPI(
		title="Warehouse Management",
		description="Welcome to Warehouse Management's API documentation!",
		redoc_url=None,
	)
	application.include_router(app_info)
	application.include_router(asset_group_router)
	application.include_router(responsible_router)
	application.include_router(storage_router)

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


# @app.exception_handler(IntegrityError)
# async def integrity_error_handler(request, exc):
# 	raise HTTPException(
# 		status_code=422,
# 		detail=str(exc)
# 	)
