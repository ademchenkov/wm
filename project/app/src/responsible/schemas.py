from pydantic import BaseModel, UUID4, constr


# Материально-ответственный сотрудник (МОЛ)
class Responsible(BaseModel):
	#   ID МОЛ
	id: UUID4
	#   Имя
	name: constr(max_length=20)
	#   Фамилия
	surname: constr(max_length=20)
	#   Отчество
	patronymic: constr(max_length=20)
	#   Табельный номер
	employee_id: constr(max_length=5)
	#   МОЛ активен - true - он может получать и сдавать предметы со склада
	is_active: bool
	#   МОЛ в архиве - false - отображается пользователю, true - скрыт от пользователя
	is_archived: bool
	#   Может быть отредактирован (если еще не использовался)
	can_be_edited: bool


class ResponsibleIn(BaseModel):
	name: constr(max_length=20)
	surname: constr(max_length=20)
	patronymic: constr(max_length=20)
	employee_id: constr(max_length=5)


class ResponsibleOut(Responsible):
	pass