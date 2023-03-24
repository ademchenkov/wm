from tortoise.models import Model
from tortoise import fields


class FixedAsset(Model):
	id = fields.UUIDField(pk=True)
	serial_id = fields.TextField
	accounting_id = fields.TextField
	inventory_id = fields.TextField


class LongTermMaterial(Model):
	id = fields.UUIDField(pk=True)
	serial_id = fields.TextField
	accounting_id = fields.TextField
	accounting_article = fields.TextField
	inventory_id = fields.TextField


class ShortTermMaterial(Model):
	id = fields.UUIDField(pk=True)
	accounting_article = fields.TextField
	inventory_id = fields.TextField