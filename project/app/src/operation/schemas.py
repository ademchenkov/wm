from typing import Literal

from pydantic import BaseModel, UUID4, constr


# Операция

# Типы операций:

# ARRIVAL_TO_STORAGE - поступление на склад
# PRIMARY_DELIVERY_TO_WORKPLACE - первичная выдача со склада
# REPEATED_DELIVERY_TO_WORKPLACE - повторная выдача со склада
# TRANSFER_BETWEEN_WORKPLACES - перемещение между рабочими местами
# TRANSFER_BETWEEN_RESPONSIBLES - перемещение между МОЛ
# RETURN_TO_STORAGE - возврат на склад
# WRITE_OFF_FROM_STORAGE - списание со склада
# WRITE_OFF_FROM_WORKPLACE - списание с рабочего места


# Состояния операции:

# AUTHORIZATION
# COMPLETED
# REVERSED

class OperationIn(BaseModel):
	#   Тип номенклатуры
	type: Literal[
		"ARRIVAL_TO_STORAGE",
		"PRIMARY_DELIVERY_TO_WORKPLACE",
		"REPEATED_DELIVERY_TO_WORKPLACE",
		"TRANSFER_BETWEEN_WORKPLACES",
		"TRANSFER_BETWEEN_RESPONSIBLES",
		"RETURN_TO_STORAGE",
		"WRITE_OFF_FROM_STORAGE",
		"WRITE_OFF_FROM_WORKPLACE",
	]
	# Учетная запись исполнителя
	author: constr(max_length=40)


class Operation(OperationIn):
	# ID операции
	id: UUID4
	# Состояние операции
	state: Literal[
		"COMPLETED",
		"REVERSED",
	]
	# Реверс операция false - обычная операция, true - операция отмены предыдущей операции
	is_reverse: bool
	# ID операции, которая была отменена данной операцией
	reversed_operation_id: str


class OperationOut(Operation):
	pass