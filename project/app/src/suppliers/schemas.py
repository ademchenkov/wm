from pydantic import UUID4
from pydantic import constr

from project.app.src.common.schemas import MyAbstractPydanticModel
from project.app.src.common.schemas import ObjectStatusPydanticMixin

class SupplierIn(MyAbstractPydanticModel):
	name: constr(max_length=40)
	inn: constr(max_length=12)
	signatory: constr(max_length=40)


class Supplier(SupplierIn, ObjectStatusPydanticMixin):
	id: UUID4


class SupplierOut(Supplier):
	pass