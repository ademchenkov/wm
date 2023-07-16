from pydantic import UUID4, constr

from project.app.src.common.schemas import MyAbstractPydanticModel
from project.app.src.common.schemas import ObjectStatusPydanticMixin


# Материально-ответственный сотрудник (МОЛ)


class ResponsibleIn(MyAbstractPydanticModel):
	#   Имя
	name: constr(max_length=20)
	#   Фамилия
	surname: constr(max_length=20)
	#   Отчество
	patronymic: constr(max_length=20)
	#   Табельный номер
	employee_id: constr(max_length=5)


class Responsible(ResponsibleIn, ObjectStatusPydanticMixin):
	#   ID МОЛ
	id: UUID4


class ResponsibleOut(Responsible):
	pass
