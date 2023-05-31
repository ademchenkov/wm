from fastapi import APIRouter

from project.app.src.config import get_settings

router = APIRouter(
	include_in_schema=False
)
settings = get_settings()


@router.get("/")
async def get_app_info():
	return {
		"app_name": settings.app_name,
		"environment": settings.environment,
		"is_testing": settings.testing,
	}
