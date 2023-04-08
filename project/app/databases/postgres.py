import logging

from fastapi import FastAPI
from tortoise import Tortoise
from tortoise import run_async
from tortoise.contrib.fastapi import register_tortoise

from project.app.config.PostgresConfig import TORTOISE_ORM


async def init_db(app: FastAPI) -> None:
	await Tortoise.init(config=TORTOISE_ORM)
	register_tortoise(
		app,
		config=TORTOISE_ORM,
		generate_schemas=True,
		add_exception_handlers=True,
	)


async def generate_schema() -> None:
	logging.info("Initializing Tortoise...")

	await Tortoise.init(config=TORTOISE_ORM)
	logging.info("Generating database schema via Tortoise...")
	await Tortoise.generate_schemas()
	await Tortoise.close_connections()


if __name__ == "__main__":
	run_async(generate_schema())
