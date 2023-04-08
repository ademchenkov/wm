from tortoise.models import Model
from tortoise import fields

from project.app.config.AppConfig import ASSET_GROUP_PREFIX


class AssetGroup(Model):
	id = fields.CharField(pk=True, max_length=10)
	type = fields.CharField(null=False, max_length=20)
	short_name = fields.CharField(unique=True, max_length=30)
	full_name = fields.CharField(unique=True, max_length=150)
	amount_remains_in_storage = fields.FloatField(default=0)
	amount_in_use = fields.FloatField(default=0)

	def __str__(self):
		return self.short_name

	async def generate_id(self):
		prefix = ASSET_GROUP_PREFIX
		rows_count = await AssetGroup.all().count()
		sequence_number_str = "{:07d}".format(rows_count + 1)
		self.id = f"{prefix}{sequence_number_str}"

	@staticmethod
	async def create_with_id(asset_group_type, short_name, full_name):
		test_model = AssetGroup(
			type=asset_group_type,
			short_name=short_name,
			full_name=full_name,
			amount_remains_in_storage=0,
			amount_in_use=0,
		)
		await test_model.generate_id()
		await test_model.save()
		return test_model