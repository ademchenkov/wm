from pydantic import BaseModel
from pydantic.fields import Optional


#  ТМЦ длительного пользования
class LongTermMaterial(BaseModel):

	# Id номенклатуры
	asset_group_id: str

	# Серийный номер
	serial_id: Optional[str] = None

	# Бухгалтерский инвентарный номер
	accounting_id: Optional[str] = None

	# Бухгалтерский артикул
	accounting_article: Optional[str] = None

	# Складской инвентарный номер
	inventory_id: str
