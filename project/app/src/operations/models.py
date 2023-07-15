from uuid import UUID

from tortoise import fields

from project.app.src.common.models import MyAbstractBaseModel
from project.app.src.common.models import TimestampMixin


class OperationDb(MyAbstractBaseModel, TimestampMixin):
	id: str = fields.UUIDField(pk=True)
	type: str = fields.CharField(null=False, max_length=40)
	state: str = fields.CharField(null=False, max_length=20)
	is_reverse: bool = fields.BooleanField(null=False)
	reversed_operation_id: fields.ForeignKeyNullableRelation["OperationDb"] = fields.ForeignKeyField(
		"models.OperationDb", related_name="main_operation", null=True, on_delete=fields.SET_NULL
	)
	author: str = fields.CharField(null=True, max_length=40)

	def __str__(self):
		return "operations = " + self.id

	# Класс для определения дополнительных настроек модели
	class Meta:
		# Имя таблицы в БД
		table = "operations"

	@staticmethod
	async def create(operation_in: dict):
		operation = OperationDb(
			type=operation_in["type"],
			state="COMPLETED",
			author=operation_in["author"]
		)
		await operation.save()
		return operation
