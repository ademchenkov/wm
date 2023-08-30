from project.app.src.common.schemas import MyAbstractPydanticModel


class GetAssetsToWarehouseIn(MyAbstractPydanticModel):
	responsible: str
	storage: str


