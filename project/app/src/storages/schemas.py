from pydantic import constr

from project.app.src.common.schemas import MyAbstractPydanticModel
from project.app.src.common.schemas import ObjectStatusPydanticMixin


# Склад
class StorageIn(MyAbstractPydanticModel):
	#   Название склада (естественный ID)
	name: constr(max_length=20, to_upper=True, strip_whitespace=True)


class Storage(StorageIn, ObjectStatusPydanticMixin):
	# ID МОЛ cклада
	responsible_id: str | None


class StorageOut(Storage):
	pass