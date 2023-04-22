from typing import Any

from fastapi import APIRouter, HTTPException
from tortoise.exceptions import DoesNotExist

from project.app.src.asset_group.service import create_asset_group
from project.app.src.asset_group.service import delete_asset_group
from project.app.src.asset_group.service import get_all_asset_groups
from project.app.src.asset_group.service import get_asset_group_by_id
from project.app.src.asset_group.service import update_asset_group
from project.app.src.asset_group.schemas import AssetGroupIn
from project.app.src.asset_group.schemas import AssetGroupOut
from project.app.src.common.async_context_manager import AsyncContextManager

router = APIRouter()


@router.get("/asset-groups", status_code=200, response_model=list[AssetGroupOut], description="Получить список номенклатур")
async def get_asset_groups(
		is_active: bool = True,
		is_archived: bool = False,
) -> Any:
	return await get_all_asset_groups(is_active=is_active, is_archived=is_archived)


@router.get("/asset-groups/{asset_group_id}", status_code=200, response_model=AssetGroupOut, description="Получить номенклатуру по id")
async def get_asset_group(asset_group_id: str):
	try:
		return await get_asset_group_by_id(asset_group_id)
	except DoesNotExist:
		raise HTTPException(status_code=404, detail="Asset group not found")


@router.post("/asset-groups", status_code=201, response_model=AssetGroupOut, description="Создать новую номенклатуру")
async def create_new_asset_group(asset: AssetGroupIn):
	return await create_asset_group(asset)


@router.put("/asset-groups/{asset_group_id}", status_code=200, response_model=AssetGroupOut, description="Редактировать новую номенклатуру")
async def update_asset_group_by_id(asset_group_id: str, payload: AssetGroupIn):
	try:
		asset_group = await get_asset_group_by_id(asset_group_id)
	except DoesNotExist:
		raise HTTPException(status_code=404, detail=f"Asset group {asset_group_id} not found")
	if not asset_group.can_be_edited:
		raise HTTPException(status_code=400, detail=f"Cannot update asset group {asset_group_id}")
	async with AsyncContextManager():
		updated_asset_group = await update_asset_group(asset_group_id, payload)
	return updated_asset_group


@router.delete(
	"/asset-groups/{asset_group_id}", status_code=200, response_model=AssetGroupOut, description="Отправить номенклатуру в архив")
async def delete_asset_group_by_id(asset_group_id: str):
	try:
		asset_group = await get_asset_group_by_id(asset_group_id)
	except DoesNotExist:
		raise HTTPException(status_code=404, detail=f"Asset group {asset_group_id} not found")
	if not asset_group.can_be_edited or asset_group.amount_in_use != 0 or asset_group.amount_remains_in_storage != 0:
		raise HTTPException(status_code=400, detail=f"Cannot archive asset group {asset_group_id}")
	if asset_group.is_archived:
		raise HTTPException(status_code=400, detail=f"Asset group {asset_group_id} is already archived")
	async with AsyncContextManager():
		updated_asset_group = await delete_asset_group(asset_group_id)
	return updated_asset_group
