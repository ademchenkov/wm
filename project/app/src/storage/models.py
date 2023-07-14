from tortoise import fields

from project.app.src.common.models import MyAbstractBaseModel
from project.app.src.common.models import ObjectStatusMixin
from project.app.src.common.models import TimestampMixin


class StorageDb(MyAbstractBaseModel, ObjectStatusMixin, TimestampMixin):
	name = fields.CharField(pk=True, null=False, max_length=20)

	def __str__(self):
		return "storage_name = " + self.name

	# Класс для определения дополнительных настроек модели
	class Meta:
		# Имя таблицы в БД
		table = "storages"

	@staticmethod
	async def create(storage_in: dict):
		storage = StorageDb(
			name=storage_in["name"],
		)
		await storage.save()
		return storage