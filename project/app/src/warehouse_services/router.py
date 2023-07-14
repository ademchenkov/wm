from typing import Any

from fastapi import APIRouter, HTTPException
from fastapi import status

from project.app.src.common.async_context_manager import AsyncContextManager
from project.app.src.responsible.models import ResponsibleDb
from project.app.src.storage.models import StorageDb
from project.app.src.warehouse_services.schemas import StorageResponsibleOut
from project.app.src.warehouse_services.service import define_responsible_to_storage

router = APIRouter(
	prefix="/warehouse-services",
	tags=["Warehouse-services"],
)


@router.put(
	"/storage/{storage_name}/responsible/{responsible_id}",
	status_code=status.HTTP_200_OK,
	response_model=StorageResponsibleOut,
)
async def define_responsible(storage_name: str, responsible_id: str) -> Any:
	existing_storage = await StorageDb.get_or_none(name=storage_name)
	if not existing_storage:
		raise HTTPException(
			status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
			detail="Storage name is not correct"
		)
	existing_responsible = await ResponsibleDb.get_or_none(id=responsible_id)
	if not existing_responsible:
		raise HTTPException(
			status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
			detail="Responsible name is not correct"
		)
	async with AsyncContextManager():
		defined_responsible = await define_responsible_to_storage(storage_name, responsible_id)
	return defined_responsible
