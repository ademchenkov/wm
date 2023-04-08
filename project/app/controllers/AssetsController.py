from typing import List

from project.app.models.pydantic.AssetGroupPydantic import AssetGroupIn
from project.app.models.pydantic.AssetGroupPydantic import AssetGroupOut
from project.app.models.tortoise.AssetGroupTortoise import AssetGroup


async def create_asset_group(asset_group: AssetGroupIn) -> AssetGroupOut:
	created_asset_group = await AssetGroup.create_with_id(
		asset_group_type=asset_group.type,
		short_name=asset_group.short_name,
		full_name=asset_group.full_name,
	)

	return AssetGroupOut(**dict(created_asset_group))


async def get_all_asset_groups() -> List[AssetGroup]:
	return await AssetGroup.all()


async def get_asset_group_by_id(asset_group_id: str) -> AssetGroup:
	return await AssetGroup.filter(id=asset_group_id).get().values()