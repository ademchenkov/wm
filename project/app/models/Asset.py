from pydantic import BaseModel, Field, UUID4, confloat, constr
from pydantic.fields import Optional

from project.app.models.FixedAsset import FixedAsset
from project.app.models.LongTermMaterial import LongTermMaterial
from project.app.models.ShortTermMaterial import ShortTermMaterial


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
