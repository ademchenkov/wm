from pydantic import BaseModel, UUID4, constr


# Склад
class Storage(BaseModel):
	#   ID склада
	id: UUID4
	#   Название склада
	name: constr(max_length=20)
	#   Склад активен - true - можно получать и сдавать предметы со склада
	is_active: bool
	#   Склад в архиве - false - отображается пользователю, true - скрыт от пользователя
	is_archived: bool
	#   Может быть отредактирован (если еще не использовался)
	can_be_edited: bool


class StorageIn(BaseModel):
	name: constr(max_length=20)


class StorageOut(Storage):
	pass