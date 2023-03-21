from fastapi import APIRouter

from ..config import get_settings

router = APIRouter(
	prefix="/info",
	tags=["info"],
)
settings = get_settings()


@router.get("/")
async def info():
	return {
		"app_name": settings.app_name,
		"environment": settings.environment,
		"is_testing": settings.is_testing,
	}
