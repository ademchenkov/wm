from pydantic import BaseModel
from pydantic.fields import Optional


#  ТМЦ - расходные (учитываются партией)
class ShortTermMaterial(BaseModel):
	#  Бухгалтерский артикул
	accounting_article: Optional[str] = None

	#  Складской инвентарный номер
	inventory_id: str