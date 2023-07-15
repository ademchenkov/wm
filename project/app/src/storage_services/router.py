from typing import Any

from fastapi import APIRouter, status, HTTPException

from project.app.src.responsibles.models import ResponsibleDb
from project.app.src.storage_services.service import define_responsible_to_storage
from project.app.src.storages.models import StorageDb
from project.app.src.storages.schemas import StorageOut

router = APIRouter(
	prefix="/storage-services",
	tags=["Storage-services"],
)


@router.put(
	"/storages/{storage_name}/responsibles/{responsible_id}",
	status_code=status.HTTP_200_OK,
	response_model=StorageOut,
)
async def define_responsible(storage_name: str, responsible_id: str) -> Any:
	existing_storage = await StorageDb.get_or_none(storage_name=storage_name)
	existing_responsible = await ResponsibleDb.get_or_none(responsible_id=responsible_id)
	if not existing_storage or existing_responsible:
		raise HTTPException(
			status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
			detail="Couldn't define responsible. Check if storage and responsible exists"
		)
	storage_with_defined_responsible = await define_responsible_to_storage(storage_name, responsible_id)
	return storage_with_defined_responsible