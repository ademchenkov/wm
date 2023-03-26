from typing import List

from project.app.models.pydantic.AssetGroupPydantic import AssetGroupIn
from project.app.models.pydantic.AssetGroupPydantic import AssetGroupOut
from project.app.models.tortoise.AssetGroupTortoise import AssetGroup
from project.app.services.AsyncContextManager import AsyncContextManager
from project.app.exceptions.Exceptions import Exceptions

exceptions = Exceptions()


async def create_asset_group(asset_group: AssetGroupIn) -> AssetGroupOut:
	created_asset_group = await AssetGroup.create_with_id(
		asset_group_type=asset_group.type,
		short_name=asset_group.short_name,
		full_name=asset_group.full_name,
	)

	return AssetGroupOut(**dict(created_asset_group))


async def get_all_asset_groups(is_active: bool, is_archived: bool) -> List[AssetGroup]:
	return await AssetGroup.filter(is_active=is_active, is_archived=is_archived)


async def get_asset_group_by_id(asset_group_id: str) -> AssetGroup:
	return await AssetGroup.get(id=asset_group_id)


async def update_asset_group(asset_group_id: str, asset_group: AssetGroupIn) -> AssetGroup | Exception:
	async with AsyncContextManager():
		asset_group_obj = await AssetGroup.filter(id=asset_group_id).select_for_update().first()
		if asset_group_obj and asset_group_obj.can_be_edited:
			await AssetGroup.filter(id=asset_group_id).update(**asset_group.dict())
			return await get_asset_group_by_id(asset_group_id)
		if not asset_group_obj:
			return exceptions.get_exception_text('AssetGroup', 'AG001')  # "Asset group doesn't exist"
		else:
			return exceptions.get_exception_text('AssetGroup', 'AG002')  # "Cannot update asset group"


async def delete_asset_group(asset_group_id: str) -> bool | str:
	async with AsyncContextManager():
		asset_group_obj = await AssetGroup.filter(id=asset_group_id).select_for_update().first()
		if asset_group_obj and asset_group_obj.is_archived is not True:
			asset_group_obj.can_be_edited = False
			asset_group_obj.is_archived = True
			await asset_group_obj.save()
			return f"Asset group {asset_group_id} archived successfully."
		else:
			return False
