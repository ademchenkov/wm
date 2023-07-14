from typing import Any

from fastapi import APIRouter, status, HTTPException
from tortoise.exceptions import DoesNotExist

from project.app.src.responsibles.schemas import ResponsibleIn
from project.app.src.responsibles.schemas import ResponsibleOut
from project.app.src.responsibles.service import get_all
from project.app.src.responsibles.service import create
from project.app.src.responsibles.service import get_by_id
from project.app.src.responsibles.service import update
from project.app.src.responsibles.service import delete
from project.app.src.common.async_context_manager import AsyncContextManager

router = APIRouter(
	prefix="/responsibles",
	tags=["Responsibles"],
)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[ResponsibleOut])
async def get_responsibles(
		is_active: bool = True,
		is_archived: bool = False,
) -> Any:
	return await get_all(is_active=is_active, is_archived=is_archived)


@router.get("/{responsible_id}", status_code=status.HTTP_200_OK, response_model=ResponsibleOut)
async def get_responsible_by_id(responsible_id: str) -> Any:
	try:
		return await get_by_id(responsible_id)
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Responsible not found"
		)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ResponsibleOut)
async def create_responsible(responsible: ResponsibleIn) -> Any:
	new_responsible = await create(responsible)
	if not new_responsible:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Responsible cannot be created"
		)
	return new_responsible


@router.patch("/{responsible_id}", status_code=status.HTTP_200_OK, response_model=ResponsibleOut)
async def update_responsible_by_id(responsible_id: str, payload: ResponsibleIn) -> Any:
	try:
		responsible = await get_by_id(responsible_id)
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f"Responsible: {responsible_id} not found"
		)
	if not responsible.can_be_edited:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=f"Cannot update responsibles: {responsible_id}"
		)
	async with AsyncContextManager():
		updated_responsible = await update(responsible_id, payload)
	return updated_responsible


@router.delete("/{responsible_id}", status_code=status.HTTP_200_OK, response_model=ResponsibleOut)
async def delete_responsible_by_id(responsible_id: str) -> Any:
	try:
		responsible = await get_by_id(responsible_id)
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f"Responsible: {responsible_id} not found"
		)
	if not responsible.can_be_edited:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=f"Cannot archive responsibles: {responsible_id}"
		)
	if responsible.is_archived:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=f"Responsible: {responsible_id} is already archived"
		)
	async with AsyncContextManager():
		updated_responsible = await delete(responsible_id)
	return updated_responsible