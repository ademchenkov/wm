from typing import Literal

from pydantic import constr

from project.app.src.common.schemas import MyAbstractPydanticModel
from project.app.src.common.schemas import ObjectStatusPydanticMixin


# Рабочее место
class WorkplaceIn(MyAbstractPydanticModel):
	# Наименование строения
	building: Literal["MAIN", "TEMP"]
	# Номер этажа
	floor: constr(max_length=2)
	# Номер комнаты
	room: constr(max_length=5)
	# Номер места
	place: constr(max_length=2)


class Workplace(WorkplaceIn, ObjectStatusPydanticMixin):
	#   ID рабочего места
	id: constr(max_length=40)


class WorkplaceOut(Workplace):
	pass
