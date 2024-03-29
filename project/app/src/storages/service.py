from typing import List

from project.app.src.common.async_context_manager import AsyncContextManager
from project.app.src.storages.models import StorageDb
from project.app.src.storages.schemas import StorageIn
from project.app.src.storages.schemas import StorageOut


async def create(storage: StorageIn) -> StorageOut:
	created_storage: dict = await StorageDb.create(storage.dict())
	return StorageOut(**dict(created_storage))


async def get_all(is_active: bool, is_archived: bool) -> List[StorageOut]:
	storage_list: List = await StorageDb.filter(is_active=is_active, is_archived=is_archived)
	return [StorageOut(**dict(storage_list)) for storage_list in storage_list]


async def get_by_name(storage_name: str) -> StorageOut:
	storage = await StorageDb.get(name=storage_name)
	return StorageOut(**dict(storage))


async def update(storage_name: str, storage: StorageIn) -> StorageOut:
	async with AsyncContextManager():
		storage_obj = await StorageDb.filter(name=storage_name).select_for_update().first()
		await storage_obj.update_from_dict(dict(storage))
		await storage_obj.save()
		return StorageOut(**dict(storage_obj))


async def delete(storage_name: str) -> StorageOut:
	async with AsyncContextManager():
		storage_obj = await StorageDb.filter(name=storage_name).select_for_update().first()
		storage_obj.can_be_edited = False
		storage_obj.is_archived = True
		await storage_obj.save()
		return StorageOut(**dict(storage_obj))
