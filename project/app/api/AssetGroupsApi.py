from fastapi import APIRouter, HTTPException
from tortoise.exceptions import DoesNotExist

from project.app.controllers.AssetsController import create_asset_group
from project.app.controllers.AssetsController import get_all_asset_groups
from project.app.controllers.AssetsController import get_asset_group_by_id
from project.app.models.pydantic.AssetGroupPydantic import AssetGroup
from project.app.models.pydantic.AssetGroupPydantic import AssetGroupIn
from project.app.models.pydantic.AssetGroupPydantic import AssetGroupOut

router = APIRouter()


@router.get("/asset-groups")
async def get_asset_groups():
	return await get_all_asset_groups()


@router.get("/asset-groups/{asset_group_id}", response_model=AssetGroup)
async def get_asset_group(asset_group_id):
	try:
		return await get_asset_group_by_id(asset_group_id)
	except DoesNotExist:
		raise HTTPException(status_code=404, detail="Asset group not found")


@router.post("/asset-groups", response_model=AssetGroupOut)
async def create_new_asset_group(asset: AssetGroupIn):
	return await create_asset_group(asset)

# @router.put("/assets/{asset-id}")
# def update_asset(asset_id):
# 	pass
#
#
# @router.delete("/assets/{asset-id}")
# def mark_as_unused_asset(asset_id):
# 	pass
