from typing import Literal

from pydantic import BaseModel, confloat, constr


# Номенклатура


class AssetGroupIn(BaseModel):
	#   Тип номенклатуры
	type: Literal["FIXED_ASSET", "LONG_TERM_MATERIAL", "SHORT_TERM_MATERIAL"]
	#   Короткое имя номенклатуры
	short_name: constr(max_length=30, to_upper=True, strip_whitespace=True)
	#   Полное имя номенклатуры
	full_name: constr(max_length=150, to_upper=True, strip_whitespace=True)


class AssetGroup(AssetGroupIn):
	#   ID номенклатуры
	id: constr(max_length=10)
	#   Количество на складе
	amount_remains_in_storage: confloat(ge=0)
	#   Количество в использовании
	amount_in_use: confloat(ge=0)
	#   Номенклатура активна - true - можно создавать позиции, false - нельзя создавать позиции
	is_active: bool
	#   Номенклатура в архиве - false - отображается пользователю, true - скрыта от пользователя
	is_archived: bool
	#   Может быть отредактирован (если еще не использовался)
	can_be_edited: bool


class AssetGroupOut(AssetGroup):
	pass
