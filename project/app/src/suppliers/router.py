from typing import Any

from fastapi import APIRouter, HTTPException, status
from tortoise.exceptions import DoesNotExist

from project.app.src.suppliers.service import create
from project.app.src.suppliers.service import delete
from project.app.src.suppliers.service import get_all
from project.app.src.suppliers.service import get_by_id
from project.app.src.suppliers.service import update
from project.app.src.suppliers.schemas import SupplierIn
from project.app.src.suppliers.schemas import SupplierOut
from project.app.src.common.async_context_manager import AsyncContextManager

router = APIRouter(
	prefix="/suppliers",
	tags=["Suppliers"],
)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[SupplierOut])
async def get_suppliers(
		is_active: bool = True,
		is_archived: bool = False,
) -> Any:
	return await get_all(is_active=is_active, is_archived=is_archived)


@router.get("/{supplier_id}", status_code=status.HTTP_200_OK, response_model=SupplierOut)
async def get_supplier_by_id(supplier_id: str) -> Any:
	try:
		return await get_by_id(supplier_id)
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Supplier not found"
		)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SupplierOut)
async def create_new_supplier(supplier: SupplierIn) -> Any:
	if len(supplier.inn) not in (10, 12):
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="INN should have 10 or 12 numbers"
		)
	new_supplier = await create(supplier)
	if not new_supplier:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Supplier cannot be created"
		)
	return new_supplier


@router.patch("/{supplier_id}", status_code=status.HTTP_200_OK, response_model=SupplierOut)
async def update_supplier_by_id(supplier_id: str, payload: SupplierIn) -> Any:
	try:
		supplier = await get_by_id(supplier_id)
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f"Supplier: {supplier_id} not found"
		)
	if not supplier.can_be_edited:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=f"Cannot update supplier: {supplier_id}"
		)
	async with AsyncContextManager():
		updated_supplier = await update(supplier_id, payload)
	return updated_supplier


@router.delete("/{supplier_id}", status_code=status.HTTP_200_OK, response_model=SupplierOut)
async def delete_supplier_by_id(supplier_id: str) -> Any:
	try:
		supplier = await get_by_id(supplier_id)
	except DoesNotExist:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f"Supplier {supplier_id} not found"
		)
	if not (
			supplier.can_be_edited
	):
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=f"Cannot archive supplier {supplier_id}"
		)
	if supplier.is_archived:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=f"Supplier {supplier_id} is already archived"
		)
	async with AsyncContextManager():
		updated_supplier = await delete(supplier_id)
	return updated_supplier