from fastapi import APIRouter

from project.app.config.AppConfig import get_settings

router = APIRouter()
settings = get_settings()


@router.get("/")
async def info():
	return {
		"app_name": settings.app_name,
		"environment": settings.environment,
		"is_testing": settings.testing,
	}
