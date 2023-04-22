from pydantic import BaseModel
from pydantic.fields import Optional


#  Основное средство
class FixedAsset(BaseModel):

	# Id номенклатуры
	asset_group_id: str

	# Серийный номер
	serial_id: Optional[str] = None

	# Бухгалтерский инвентарный номер
	accounting_id: str = None

	# Складской инвентарный номер
	inventory_id: str
