from tortoise import fields

from project.app.src.assets.constants import ModelPrefix
from project.app.src.common.models import MyAbstractBaseModel
from project.app.src.common.models import TimestampMixin


class AssetDb(MyAbstractBaseModel, TimestampMixin):
	id = fields.CharField(pk=True, max_length=9)
	asset_group_id = fields.ForeignKeyField(
		model_name="models.AssetGroupDb",
		related_name="assets",
		backward_key="asset_group_id",
	)
	amount_total = fields.FloatField(null=False, default=0)
	amount_in_storage = fields.FloatField(null=False, default=0)
	amount_in_workplace = fields.FloatField(null=False, default=0)
	amount_written_off = fields.FloatField(null=False, default=0)
	state = fields.CharField(null=False, max_length=20)

	def __str__(self):
		return "asset_id = " + self.id

	# Класс для определения дополнительных настроек модели
	class Meta:
		# Имя таблицы в БД
		table = "assets"

	# Генерация id с префиксом
	async def generate_id(self):
		prefix = ModelPrefix.ASSET_PREFIX
		rows_count = await AssetDb.all().count()
		sequence_number_str = "{:06d}".format(rows_count + 1)
		self.id = f"{prefix}{sequence_number_str}"

	# Создание экземпляра класса со сгенерированным id
	@staticmethod
	async def create_with_id(asset_in: dict):
		test_model = AssetDb(
			asset_group_id=asset_in["asset_group_id"],
			amount_total=asset_in["amount_total"],
			state="IN_STORAGE",
		)
		await test_model.generate_id()
		await test_model.save()
		return test_model
