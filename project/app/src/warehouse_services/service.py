from project.app.src.warehouse_services.models import StorageResponsibleDb
from project.app.src.warehouse_services.schemas import StorageResponsibleOut


# Назначить (изменить) МОЛ на складе
async def define_responsible_to_storage(storage_name: str, responsible_id: str) -> StorageResponsibleOut:
	defined_responsible = await StorageResponsibleDb.define_responsible(storage_name, responsible_id)
	return StorageResponsibleOut(**dict(defined_responsible))


# Принять материальные средства на склад
def get_assets_to_warehouse():
	pass


# Выдать со склада
def deliver_assets_from_warehouse():
	pass


# Вернуть на склад
def return_assets_to_warehouse():
	pass


# Переместить материальные средства в использовании
def transfer_assets_in_use():
	pass


# Переместить материальные ценности между складами
def transfer_assets_between_storages():
	pass


# Списать со склада
def write_off_assets_from_storage():
	pass


# Списать с рабочего места
def write_off_assets_from_workplace():
	pass


# Отменить операцию (сделать обратную проводку)
def reverse_operation():
	pass
