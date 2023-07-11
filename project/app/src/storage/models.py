from tortoise.models import Model
from tortoise import fields


class StorageDb(Model):
	id = fields.UUIDField(pk=True)
	name = fields.CharField(null=False, max_length=20)
	is_active = fields.BooleanField(null=False, default=True)
	is_archived = fields.BooleanField(null=False, default=False)
	can_be_edited = fields.BooleanField(null=False, default=True)
	created_at = fields.DatetimeField(null=False, auto_now_add=True)
	updated_at = fields.DatetimeField(auto_now=True)

	def __str__(self):
		return "storage_name = " + self.name

	# Класс для определения дополнительных настроек модели
	class Meta:
		# Имя таблицы в БД
		table = "storages"

	@staticmethod
	async def create(storage_in: dict):
		storage = StorageDb(
		)
		await storage.save()
		return storage