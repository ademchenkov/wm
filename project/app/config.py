import logging

from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
	app_name: str = "Warehouse Management"
	environment: str = "DEV"  # DEV, STAGE, PROD
	is_testing: bool = bool(0)


def get_settings() -> BaseSettings:
	log.info("Loading config settings from the environment...")
	return Settings()
