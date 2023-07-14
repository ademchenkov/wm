from typing import Any

from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist

from project.app.src.workplace.service import create
from project.app.src.workplace.service import delete
from project.app.src.workplace.service import get_all
from project.app.src.workplace.service import get_by_id
from project.app.src.workplace.schemas import WorkplaceIn
from project.app.src.workplace.schemas import WorkplaceOut
from project.app.src.common.async_context_manager import AsyncContextManager

router = APIRouter(
	prefix="/workplaces",
	tags=["Workplaces"],
)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[WorkplaceOut])
async def get_workplaces(
		is_active: bool = True,
		is_archived: bool = False,
		building: str = None,
		floor: str = None,
		room: str = None,
) -> Any:
	return await get_all(
		is_active=is_active,
		is_archived=is_archived,
		building=building,
		floor=floor,
		room=room,
	)


@router.get("/{workplace_id}", status_code=status.HTTP_200_OK, response_model=WorkplaceOut)
async def get_workplace_by_id(workplace_id: str) -> Any:
	try:
		return await get_by_id(workplace_id)
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Workplace not found"
		)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=WorkplaceOut)
async def create_new_workplace(workplace: WorkplaceIn) -> Any:
	new_workplace = await create(workplace)
	if not new_workplace:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Workplace cannot be created"
		)
	return new_workplace


@router.delete("/{workplace_id}", status_code=status.HTTP_200_OK, response_model=WorkplaceOut)
async def delete_workplace_by_id(workplace_id: str) -> Any:
	try:
		workplace = await get_by_id(workplace_id)
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f"Workplace {workplace_id} not found"
		)
	if not (
			workplace.can_be_edited
	):
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=f"Cannot archive workplace {workplace_id}"
		)
	if workplace.is_archived:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=f"Workplace {workplace_id} is already archived"
		)
	async with AsyncContextManager():
		updated_workplace = await delete(workplace_id)
	return updated_workplace
