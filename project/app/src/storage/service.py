from typing import List

from project.app.src.common.async_context_manager import AsyncContextManager
from project.app.src.storage.models import StorageDb
from project.app.src.storage.schemas import StorageIn
from project.app.src.storage.schemas import StorageOut


async def create(storage: StorageIn) -> StorageOut:
	created_storage: dict = await StorageDb.create(storage.dict())
	return StorageOut(**dict(created_storage))


async def get_all(is_active: bool, is_archived: bool) -> List[StorageOut]:
	storage_list: List = await StorageDb.filter(is_active=is_active, is_archived=is_archived)
	return [StorageOut(**dict(storage_list)) for storage_list in storage_list]


async def get_by_id(storage_id: str) -> StorageOut:
	storage = await StorageDb.get(id=storage_id)
	return StorageOut(**dict(storage))


async def update(storage_id: str, storage: StorageIn) -> StorageOut:
	async with AsyncContextManager():
		storage_obj = await StorageDb.filter(id=storage_id).select_for_update().first()
		await storage_obj.update_from_dict(dict(storage))
		await storage_obj.save()
		return StorageOut(**dict(storage_obj))


async def delete(responsible_id: str) -> StorageOut:
	async with AsyncContextManager():
		storage_obj = await StorageDb.filter(id=responsible_id).select_for_update().first()
		storage_obj.can_be_edited = False
		storage_obj.is_archived = True
		await storage_obj.save()
		return StorageOut(**dict(storage_obj))