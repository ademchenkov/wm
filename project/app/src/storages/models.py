from tortoise import fields

from project.app.src.common.models import MyAbstractBaseModel
from project.app.src.common.models import ObjectStatusMixin
from project.app.src.common.models import TimestampMixin
from project.app.src.responsibles.models import ResponsibleDb


class StorageDb(MyAbstractBaseModel, ObjectStatusMixin, TimestampMixin):
	name: str = fields.CharField(pk=True, null=False, max_length=20)
	responsible_id: fields.ForeignKeyNullableRelation["ResponsibleDb"] = fields.ForeignKeyField(
		"models.ResponsibleDb", related_name="storages", null=True, on_delete=fields.SET_NULL
	)

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
