from typing import List

from project.app.src.asset_group.schemas import AssetGroupIn
from project.app.src.asset_group.schemas import AssetGroupOut
from project.app.src.asset_group.models import AssetGroupDb
from project.app.src.common.async_context_manager import AsyncContextManager


async def create(asset_group: AssetGroupIn) -> AssetGroupOut:
	created_asset_group = await AssetGroupDb.create_with_id(
		asset_group_type=asset_group.type,
		short_name=asset_group.short_name,
		full_name=asset_group.full_name,
	)
	return AssetGroupOut(**dict(created_asset_group))


async def get_all(is_active: bool, is_archived: bool) -> List[AssetGroupOut]:
	asset_group_list: List = await AssetGroupDb.filter(is_active=is_active, is_archived=is_archived)
	return [AssetGroupOut(**dict(asset_group_list)) for asset_group_list in asset_group_list]


async def get_by_id(asset_group_id: str) -> AssetGroupOut:
	asset_group = await AssetGroupDb.get(id=asset_group_id)
	return AssetGroupOut(**dict(asset_group))


async def update(asset_group_id: str, asset_group: AssetGroupIn) -> AssetGroupOut:
	asset_group_obj = await AssetGroupDb.filter(id=asset_group_id).select_for_update().first()
	await asset_group_obj.update_from_dict(dict(asset_group))
	await asset_group_obj.save()
	return AssetGroupOut(**dict(asset_group_obj))


async def delete(asset_group_id: str) -> AssetGroupOut:
	async with AsyncContextManager():
		asset_group_obj = await AssetGroupDb.filter(id=asset_group_id).select_for_update().first()
		asset_group_obj.can_be_edited = False
		asset_group_obj.is_archived = True
		await asset_group_obj.save()
		return AssetGroupOut(**dict(asset_group_obj))
