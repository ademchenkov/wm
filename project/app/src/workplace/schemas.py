from typing import Literal

from pydantic import BaseModel, constr


# Рабочее место
class WorkplaceIn(BaseModel):
	# Наименование строения
	building: Literal["MAIN", "TEMP"]
	# Номер этажа
	floor: constr(max_length=2)
	# Номер комнаты
	room: constr(max_length=5)
	# Номер места
	place: constr(max_length=2)


class Workplace(WorkplaceIn):
	#   ID рабочего места
	id: constr(max_length=40)
	#   Рабочее место активно - true - можно создавать позиции, false - нельзя создавать позиции
	is_active: bool
	#   Рабочее место в архиве - false - отображается пользователю, true - скрыта от пользователя
	is_archived: bool
	#   Рабочее место может быть отредактировано (если еще не использовался)
	can_be_edited: bool


class WorkplaceOut(Workplace):
	pass
