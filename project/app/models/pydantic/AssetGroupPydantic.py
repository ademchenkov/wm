from typing import Literal

from pydantic import BaseModel, confloat, constr


# Номенклатура
class AssetGroup(BaseModel):

	# Id номенклатуры
	id: constr(max_length=10)

	# Тип номенклатуры
	type: Literal["FIXED_ASSET", "LONG_TERM_MATERIAL", "SHORT_TERM_MATERIAL"]

	# Короткое имя номенклатуры
	short_name: constr(max_length=30)

	# Полное имя номенклатуры
	full_name: constr(max_length=150)

	# Количество на складе
	amount_remains_in_storage: confloat(ge=0)

	# Количество в использовании
	amount_in_use: confloat(ge=0)


class AssetGroupIn(BaseModel):
	type: Literal["FIXED_ASSET", "LONG_TERM_MATERIAL", "SHORT_TERM_MATERIAL"]
	short_name: constr(max_length=30)
	full_name: constr(max_length=150)


class AssetGroupOut(BaseModel):
	id: constr(max_length=10)
	type: Literal["FIXED_ASSET", "LONG_TERM_MATERIAL", "SHORT_TERM_MATERIAL"]
	short_name: constr(max_length=30, to_upper=True, strip_whitespace=True)
	full_name: constr(max_length=150, to_upper=True, strip_whitespace=True)
	amount_remains_in_storage: confloat(ge=0)
	amount_in_use: confloat(ge=0)
