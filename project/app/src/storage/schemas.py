from pydantic import BaseModel, validator, constr


# Склад
class Storage(BaseModel):
	#   Название склада (естественный ID)
	name: constr(max_length=20, to_upper=True, strip_whitespace=True)
	#   Склад активен - true - можно получать и сдавать предметы со склада
	is_active: bool
	#   Склад в архиве - false - отображается пользователю, true - скрыт от пользователя
	is_archived: bool
	#   Может быть отредактирован (если еще не использовался)
	can_be_edited: bool


class StorageIn(BaseModel):
	name: constr(max_length=20, to_upper=True, strip_whitespace=True)


class StorageOut(Storage):
	pass
