from pydantic import BaseModel
from pydantic.fields import Optional


#  ТМЦ - расходные (учитываются партией)
class ShortTermMaterial(BaseModel):

	# Id номенклатуры
	asset_group_id: str

	# Бухгалтерский артикул
	accounting_article: Optional[str] = None

	# Складской инвентарный номер
	inventory_id: str