from tortoise import fields
from tortoise.models import Model


class MyAbstractBaseModel(Model):
	class Meta:
		abstract = True

	pass


class TimestampMixin:
	created_at = fields.DatetimeField(null=False, auto_now_add=True)
	updated_at = fields.DatetimeField(auto_now=True)


class ObjectStatusMixin:
	is_active = fields.BooleanField(null=False, default=True)
	is_archived = fields.BooleanField(null=False, default=False)
	can_be_edited = fields.BooleanField(null=False, default=True)