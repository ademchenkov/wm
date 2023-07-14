from typing import Any

from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist

from project.app.src.asset_group.service import create
from project.app.src.asset_group.service import delete
from project.app.src.asset_group.service import get_all
from project.app.src.asset_group.service import get_by_id
from project.app.src.asset_group.service import update
from project.app.src.asset_group.schemas import AssetGroupIn
from project.app.src.asset_group.schemas import AssetGroupOut
from project.app.src.common.async_context_manager import AsyncContextManager

router = APIRouter(
	prefix="/assets-groups",
	tags=["Asset Groups"],
)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[AssetGroupOut])
async def get_asset_groups(
		is_active: bool = True,
		is_archived: bool = False,
) -> Any:
	return await get_all(is_active=is_active, is_archived=is_archived)


@router.get("/{asset_group_id}", status_code=status.HTTP_200_OK, response_model=AssetGroupOut)
async def get_asset_group_by_id(asset_group_id: str) -> Any:
	try:
		return await get_by_id(asset_group_id)
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Asset group not found"
		)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AssetGroupOut)
async def create_new_asset_group(asset: AssetGroupIn) -> Any:
	new_asset_group = await create(asset)
	if not new_asset_group:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Asset group cannot be created"
		)
	return new_asset_group


@router.patch("/{asset_group_id}", status_code=status.HTTP_200_OK, response_model=AssetGroupOut)
async def update_asset_group_by_id(asset_group_id: str, payload: AssetGroupIn) -> Any:
	try:
		asset_group = await get_by_id(asset_group_id)
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f"Asset group: {asset_group_id} not found"
		)
	if not asset_group.can_be_edited:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=f"Cannot update assets group: {asset_group_id}"
		)
	async with AsyncContextManager():
		updated_asset_group = await update(asset_group_id, payload)
	return updated_asset_group


@router.delete("/{asset_group_id}", status_code=status.HTTP_200_OK, response_model=AssetGroupOut)
async def delete_asset_group_by_id(asset_group_id: str) -> Any:
	try:
		asset_group = await get_by_id(asset_group_id)
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f"Asset group {asset_group_id} not found"
		)
	if not (
			asset_group.can_be_edited
	):
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=f"Cannot archive assets group {asset_group_id}"
		)
	if asset_group.is_archived:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=f"Asset group {asset_group_id} is already archived"
		)
	async with AsyncContextManager():
		updated_asset_group = await delete(asset_group_id)
	return updated_asset_group
