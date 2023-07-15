from pydantic import BaseModel, constr


# Склад
class StorageIn(BaseModel):
	#   Название склада (естественный ID)
	name: constr(max_length=20, to_upper=True, strip_whitespace=True)


class Storage(StorageIn):
	#   Склад активен - true - можно получать и сдавать предметы со склада
	is_active: bool
	#   Склад в архиве - false - отображается пользователю, true - скрыт от пользователя
	is_archived: bool
	#   Может быть отредактирован (если еще не использовался)
	can_be_edited: bool


class StorageOut(Storage):
	# ID МОЛ cклада
	responsible_id: str | None
