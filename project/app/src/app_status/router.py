from fastapi import APIRouter

from project.app.src.config import get_settings

router = APIRouter(
	prefix="/app-status",
	tags=["App Info"],
)
settings = get_settings()


@router.get("/")
async def info():
	return {
		"app_name": settings.app_name,
		"environment": settings.environment,
		"is_testing": settings.testing,
	}
