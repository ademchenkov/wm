from typing import Any

from fastapi import APIRouter, status, HTTPException
from tortoise.exceptions import DoesNotExist

from project.app.src.storage.schemas import StorageIn
from project.app.src.storage.schemas import StorageOut
from project.app.src.storage.service import get_all
from project.app.src.storage.service import create
from project.app.src.storage.service import get_by_id
from project.app.src.storage.service import update
from project.app.src.storage.service import delete
from project.app.src.common.async_context_manager import AsyncContextManager

router = APIRouter(
	prefix="/storages",
	tags=["Storages"],
)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[StorageOut])
async def get_storages(
		is_active: bool = True,
		is_archived: bool = False,
) -> Any:
	return await get_all(is_active=is_active, is_archived=is_archived)


@router.get("/{storage-id}", status_code=status.HTTP_200_OK, response_model=StorageOut)
async def get_storage_by_id(storage_id: str) -> Any:
	try:
		return await get_by_id(storage_id)
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Storage not found"
		)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=StorageOut)
async def create_storage(storage: StorageIn) -> Any:
	new_storage = await create(storage)
	if not new_storage:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Storage cannot be created"
		)
	return new_storage


@router.patch("/{storage-id}", status_code=status.HTTP_200_OK, response_model=StorageOut)
async def update_storage_by_id(storage_id: str, payload: StorageIn) -> Any:
	try:
		storage = await get_by_id(storage_id)
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f"Storage: {storage_id} not found"
		)
	if not storage.can_be_edited:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=f"Cannot update responsible: {storage_id}"
		)
	async with AsyncContextManager():
		updated_storage = await update(storage_id, payload)
	return updated_storage


@router.delete("/{storage-id}", status_code=status.HTTP_200_OK, response_model=StorageOut)
async def delete_storage_by_id(storage_id: str) -> Any:
	try:
		storage = await get_by_id(storage_id)
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f"Storage: {storage_id} not found"
		)
	if not storage.can_be_edited:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=f"Cannot archive storage: {storage_id}"
		)
	if storage.is_archived:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=f"Storage: {storage_id} is already archived"
		)
	async with AsyncContextManager():
		updated_storage = await delete(storage_id)
	return updated_storage