from datetime import datetime

from tortoise import fields
from tortoise.models import Model


class MyAbstractBaseModel(Model):
	class Meta:
		abstract = True

	pass


class TimestampMixin:
	created_at: datetime = fields.DatetimeField(null=False, auto_now_add=True)
	updated_at: datetime = fields.DatetimeField(auto_now=True)


class ObjectStatusMixin:
	is_active: bool = fields.BooleanField(null=False, default=True)
	is_archived: bool = fields.BooleanField(null=False, default=False)
	can_be_edited: bool = fields.BooleanField(null=False, default=True)