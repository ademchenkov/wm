from typing import Any

from fastapi import APIRouter, status, HTTPException

from project.app.src.storages.schemas import StorageOut

router = APIRouter(
	prefix="/storages-services",
	tags=["Storage-services"],
)


@router.put(
	"/storages/{storage_name}/responsibles/{responsible_id}",
	status_code=status.HTTP_200_OK,
	response_model=StorageOut,
)
async def define_responsible_to_storage(storage_name: str, responsible_id: str) -> Any:
	pass
