from typing import List

from project.app.src.common.async_context_manager import AsyncContextManager
from project.app.src.responsible.models import ResponsibleDb
from project.app.src.responsible.schemas import ResponsibleIn
from project.app.src.responsible.schemas import ResponsibleOut


async def create(responsible: ResponsibleIn) -> ResponsibleOut:
	created_responsible: dict = await ResponsibleDb.create(responsible.dict())
	return ResponsibleOut(**dict(created_responsible))


async def get_all(is_active: bool, is_archived: bool) -> List[ResponsibleOut]:
	responsible_list: List = await ResponsibleDb.filter(is_active=is_active, is_archived=is_archived)
	return [ResponsibleOut(**dict(responsible_list)) for responsible_list in responsible_list]


async def get_by_id(responsible_id: str) -> ResponsibleOut:
	responsible = await ResponsibleDb.get(id=responsible_id)
	return ResponsibleOut(**dict(responsible))


async def update(responsible_id: str, responsible: ResponsibleIn) -> ResponsibleOut:
	async with AsyncContextManager():
		responsible_obj = await ResponsibleDb.filter(id=responsible_id).select_for_update().first()
		await responsible_obj.update_from_dict(dict(responsible))
		await responsible_obj.save()
		return ResponsibleOut(**dict(responsible_obj))


async def delete(responsible_id: str) -> ResponsibleOut:
	async with AsyncContextManager():
		responsible_obj = await ResponsibleDb.filter(id=responsible_id).select_for_update().first()
		responsible_obj.can_be_edited = False
		responsible_obj.is_archived = True
		await responsible_obj.save()
		return ResponsibleOut(**dict(responsible_obj))
