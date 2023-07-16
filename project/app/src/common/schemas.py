from pydantic import BaseModel


class MyAbstractPydanticModel(BaseModel):
	class Meta:
		abstract = True

	pass


class ObjectStatusPydanticMixin:
	#   Объект активен - true - можно с ним взаимодействовать
	is_active: bool
	#   Объект в архиве - false - отображается пользователю, true - скрыт от пользователя
	is_archived: bool
	#   Объект может быть отредактирован (если еще не использовался)
	can_be_edited: bool
