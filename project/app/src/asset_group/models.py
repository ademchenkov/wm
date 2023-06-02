from tortoise.models import Model
from tortoise import fields

from project.app.src.asset_group.constants import ModelPrefix


class AssetGroupDb(Model):
	id = fields.CharField(pk=True, max_length=10)
	type = fields.CharField(null=False, max_length=20)
	short_name = fields.CharField(null=False, unique=True, max_length=30)
	full_name = fields.CharField(null=False, unique=True, max_length=150)
	amount_remains_in_storage = fields.FloatField(null=False, default=0)
	amount_in_use = fields.FloatField(null=False, default=0)
	is_active = fields.BooleanField(null=False, default=True)
	is_archived = fields.BooleanField(null=False, default=False)
	can_be_edited = fields.BooleanField(null=False, default=True)
	created_at = fields.DatetimeField(null=False, auto_now_add=True)
	updated_at = fields.DatetimeField(auto_now=True)

	def __str__(self):
		return self.short_name

	# Класс для определения дополнительных настроек модели
	class Meta:
		# Имя таблицы в БД
		table = "asset_groups"

	# Генерация id с префиксом
	async def generate_id(self):
		prefix = ModelPrefix.ASSET_GROUP_PREFIX
		rows_count = await AssetGroupDb.all().count()
		sequence_number_str = "{:07d}".format(rows_count + 1)
		self.id = f"{prefix}{sequence_number_str}"

	# Создание экземпляра класса со сгенерированным id
	@staticmethod
	async def create_with_id(asset_group_type: str, short_name: str, full_name: str):
		test_model = AssetGroupDb(
			type=asset_group_type,
			short_name=short_name,
			full_name=full_name,
			amount_remains_in_storage=0,
			amount_in_use=0,
		)
		await test_model.generate_id()
		await test_model.save()
		return test_model
