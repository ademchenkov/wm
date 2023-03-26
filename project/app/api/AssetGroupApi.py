from typing import Any

from fastapi import APIRouter, HTTPException
from tortoise.exceptions import DoesNotExist

from project.app.controllers.AssetGroupControllers import create_asset_group
from project.app.controllers.AssetGroupControllers import delete_asset_group
from project.app.controllers.AssetGroupControllers import get_all_asset_groups
from project.app.controllers.AssetGroupControllers import get_asset_group_by_id
from project.app.controllers.AssetGroupControllers import update_asset_group
from project.app.models.pydantic.AssetGroupPydantic import AssetGroup
from project.app.models.pydantic.AssetGroupPydantic import AssetGroupIn
from project.app.models.pydantic.AssetGroupPydantic import AssetGroupOut

router = APIRouter()


@router.get("/asset-groups", response_model=list[AssetGroup])
async def get_asset_groups(
		is_active: bool = True,
		is_archived: bool = False,
) -> Any:
	return await get_all_asset_groups(is_active=is_active, is_archived=is_archived)


@router.get("/asset-groups/{asset_group_id}", response_model=AssetGroup)
async def get_asset_group(asset_group_id):
	try:
		return await get_asset_group_by_id(asset_group_id)
	except DoesNotExist:
		raise HTTPException(status_code=404, detail="Asset group not found")


@router.post("/asset-groups", response_model=AssetGroupOut)
async def create_new_asset_group(asset: AssetGroupIn):
	return await create_asset_group(asset)


@router.put("/asset-groups/{asset_group_id}", response_model=AssetGroup | str)
async def update_asset_group_by_id(asset_group_id, update_payload: AssetGroupIn):
	try:
		result = await update_asset_group(asset_group_id, update_payload)
		if isinstance(result, Exception):
			raise HTTPException(status_code=400, detail=result)
		return result
	except DoesNotExist:
		raise HTTPException(status_code=404, detail="Asset group not found")


@router.delete("/asset-groups/{asset_group_id}")
async def archive_asset_group(asset_group_id):
	try:
		result = await delete_asset_group(asset_group_id)
		if isinstance(result, bool):
			raise HTTPException(status_code=400, detail=f"Asset group {asset_group_id} is already archived.")
		return result
	except DoesNotExist:
		raise HTTPException(status_code=404, detail="Asset group not found")
