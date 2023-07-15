# Назначить (изменить) МОЛ на складе
from project.app.src.common.async_context_manager import AsyncContextManager
from project.app.src.storages.models import StorageDb
from project.app.src.storages.schemas import StorageOut


async def define_responsible_to_storage(storage_name: str, responsible_id: str) -> StorageOut:
	async with AsyncContextManager():
		storage_obj = await StorageDb.filter(storage_name=storage_name).select_for_update().first()
		storage_obj.responsible = responsible_id
		await storage_obj.save()
		return StorageOut(**dict(storage_obj))