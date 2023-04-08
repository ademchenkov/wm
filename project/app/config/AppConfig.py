import logging
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger("uvicorn")

# tortoise model ID prefixes
ASSET_GROUP_PREFIX = "НМК"


class Settings(BaseSettings):
	app_name: str = "Warehouse Management"
	environment: str = "DEV"  # DEV, TEST, PROD
	testing: bool = bool(0)
	database_url: AnyUrl = None


#  @lru_cache - декоратор для кеширования результата выполнения функции в память
@lru_cache()
def get_settings() -> BaseSettings:
	log.info("Loading config settings from the environment...")
	return Settings()
