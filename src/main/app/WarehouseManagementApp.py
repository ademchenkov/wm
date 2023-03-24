from fastapi import FastAPI, Request, Response

from .routers import info, assets


def create_application() -> FastAPI:
	application = FastAPI()
	application.include_router(info.router)
	application.include_router(assets.router)

	return application


app = create_application()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
	response = Response("Internal server error", status_code=500)
	try:
		request.state.db = SessionLocal()
		response = await call_next(request)
	finally:
		request.state.db.close()
	return response
