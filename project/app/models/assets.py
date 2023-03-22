from pydantic import BaseModel, Field, UUID4, confloat, constr
from pydantic.fields import Optional


#  Основное средство
class FixedAsset(BaseModel):
	#  Серийный номер
	serial_number: Optional[str] = None

	#  Бухгалтерский инвентарный номер
	accounting_unique_number: str = None

	#  Складской инвентарный номер
	inventory_number: str


# ТМЦ длительного пользования
class LongTermMaterial(BaseModel):
	#  Серийный номер
	serial_number: Optional[str] = None

	#  Бухгалтерский инвентарный номер
	accounting_unique_number: Optional[str] = None

	#  Бухгалтерский артикул
	accounting_group_number: Optional[str] = None

	#  Складской инвентарный номер
	inventory_number: str


class ShortTermMaterial(BaseModel):
	#  Бухгалтерский артикул
	accounting_group_number: Optional[str] = None

	#  Складской инвентарный номер
	inventory_number: str


#  Номенклатура
class Asset(BaseModel):
	#  id номенклатуры
	id: UUID4

	# тип номенклатуры
	type: FixedAsset | LongTermMaterial | ShortTermMaterial = Field(..., discriminator="asset_type")

	#  короткое имя номенклатуры
	short_name: constr(max_length=30)

	#  полное имя номенклатуры
	full_name: str

	#  количество на складе
	quantity_remains_in_storage: Optional[confloat](ge=0)

	# количество в использовании
	quantity_using: Optional[confloat](ge=0)
