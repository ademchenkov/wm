from tortoise import fields

from project.app.src.common.models import MyAbstractBaseModel
from project.app.src.common.models import TimestampMixin


class StorageResponsibleDb(MyAbstractBaseModel, TimestampMixin):
	id = fields.UUIDField(pk=True)
	storage_name = fields.ForeignKeyField(
		"models.StorageDb",
		related_name="storages",
		backward_key="storage_name",
	)
	responsible_id = fields.ForeignKeyField(
		"models.ResponsibleDb",
		related_name="responsibles",
		backward_key="responsible_id",
	)

	def __str__(self):
		return "storage_responsible = " + self.id

	# Класс для определения дополнительных настроек модели
	class Meta:
		# Имя таблицы в БД
		table = "storage_responsible"

	@staticmethod
	async def define_responsible(storage_name: str, responsible_id: str):
		storage_responsible = StorageResponsibleDb(
			storage_name=storage_name,
			responsible_id=responsible_id,
		)
		await storage_responsible.save()
		return storage_responsible