from tortoise.models import Model
from tortoise import fields


class Asset(Model):
	id = fields.UUIDField(pk=True)  # UUID4 generator by default
	type = fields.CharField(null=False, max_length=20)
	short_name = fields.CharField(unique=True, max_length=30)
	full_name = fields.CharField(unique=True, max_length=150)
	quantity_remains_in_storage = fields.FloatField(default=0)
	quantity_using = fields.FloatField(default=0)

	def __str__(self):
		return self.type