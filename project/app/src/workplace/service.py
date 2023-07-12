from typing import List

from project.app.src.workplace.schemas import WorkplaceIn
from project.app.src.workplace.schemas import WorkplaceOut
from project.app.src.workplace.models import WorkplaceDb
from project.app.src.common.async_context_manager import AsyncContextManager


async def create(workplace: WorkplaceIn) -> WorkplaceOut:
	created_workplace = await WorkplaceDb.create_with_id(
		building=workplace.building,
		floor=workplace.floor,
		room=workplace.room,
		place=workplace.place,
	)
	return WorkplaceOut(**dict(created_workplace))


async def get_all(
		is_active: bool,
		is_archived: bool,
		building: str | None,
		floor: str | None,
		room: str | None,
		) -> List[WorkplaceOut]:

	workplace_list: List = await WorkplaceDb.filter(
		is_active=is_active,
		is_archived=is_archived,
		**{'building': building} if building else {},
		**{'floor': floor} if floor else {},
		**{'room': room} if room else {},
	)
	return [WorkplaceOut(**dict(workplace_list)) for workplace_list in workplace_list]


async def get_by_id(workplace_id: str) -> WorkplaceOut:
	workplace = await WorkplaceDb.get(id=workplace_id)
	return WorkplaceOut(**dict(workplace))


async def delete(workplace_id: str) -> WorkplaceOut:
	async with AsyncContextManager():
		workplace_obj = await WorkplaceDb.filter(id=workplace_id).select_for_update().first()
		workplace_obj.can_be_edited = False
		workplace_obj.is_archived = True
		await workplace_obj.save()
		return WorkplaceOut(**dict(workplace_obj))