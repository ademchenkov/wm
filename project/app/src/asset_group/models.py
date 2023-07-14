from tortoise import fields

from project.app.src.asset_group.constants import ModelPrefix
from project.app.src.common.models import MyAbstractBaseModel
from project.app.src.common.models import ObjectStatusMixin
from project.app.src.common.models import TimestampMixin


class AssetGroupDb(MyAbstractBaseModel, TimestampMixin, ObjectStatusMixin):
	id = fields.CharField(pk=True, max_length=10)
	type = fields.CharField(null=False, max_length=20)
	short_name = fields.CharField(null=False, unique=True, max_length=30)
	full_name = fields.CharField(null=False, unique=True, max_length=150)

	def __str__(self):
		return "asset_group_name = " + self.short_name

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
		)
		await test_model.generate_id()
		await test_model.save()
		return test_model
