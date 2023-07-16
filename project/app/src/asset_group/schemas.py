from typing import Literal

from pydantic import constr

from project.app.src.common.schemas import MyAbstractPydanticModel
from project.app.src.common.schemas import ObjectStatusPydanticMixin


# Номенклатура


class AssetGroupIn(MyAbstractPydanticModel):
	#   Тип номенклатуры
	type: Literal["FIXED_ASSET", "LONG_TERM_MATERIAL", "SHORT_TERM_MATERIAL"]
	#   Короткое имя номенклатуры
	short_name: constr(max_length=30, to_upper=True, strip_whitespace=True)
	#   Полное имя номенклатуры
	full_name: constr(max_length=150, to_upper=True, strip_whitespace=True)


class AssetGroup(AssetGroupIn, ObjectStatusPydanticMixin):
	#   ID номенклатуры
	id: constr(max_length=10)


class AssetGroupOut(AssetGroup):
	pass
