from typing import List

from project.app.src.common.async_context_manager import AsyncContextManager
from project.app.src.suppliers.models import SupplierDb
from project.app.src.suppliers.schemas import SupplierIn
from project.app.src.suppliers.schemas import SupplierOut


async def create(supplier: SupplierIn) -> SupplierOut:
	created_supplier: dict = await SupplierDb.create(supplier.dict())
	return SupplierOut(**dict(created_supplier))


async def get_all(is_active: bool, is_archived: bool) -> List[SupplierOut]:
	supplier_list: List = await SupplierDb.filter(is_active=is_active, is_archived=is_archived)
	return [SupplierOut(**dict(supplier_list)) for supplier_list in supplier_list]


async def get_by_id(supplier_id: str) -> SupplierOut:
	supplier = await SupplierDb.get(id=supplier_id)
	return SupplierOut(**dict(supplier))


async def update(supplier_id: str, supplier: SupplierIn) -> SupplierOut:
	async with AsyncContextManager():
		supplier_obj = await SupplierDb.filter(id=supplier_id).select_for_update().first()
		await supplier_obj.update_from_dict(dict(supplier))
		await supplier_obj.save()
		return SupplierOut(**dict(supplier_obj))


async def delete(supplier_id: str) -> SupplierOut:
	async with AsyncContextManager():
		supplier_obj = await SupplierDb.filter(id=supplier_id).select_for_update().first()
		supplier_obj.can_be_edited = False
		supplier_obj.is_archived = True
		await supplier_obj.save()
		return SupplierOut(**dict(supplier_obj))