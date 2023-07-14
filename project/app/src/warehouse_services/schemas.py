from pydantic import BaseModel
from pydantic import UUID4


class StorageResponsibleOut(BaseModel):
	id: UUID4
	storage_name: str
	responsible_id: UUID4

