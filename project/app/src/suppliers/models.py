from tortoise import fields

from project.app.src.common.models import MyAbstractBaseModel
from project.app.src.common.models import ObjectStatusMixin
from project.app.src.common.models import TimestampMixin


class SupplierDb(MyAbstractBaseModel, ObjectStatusMixin, TimestampMixin):
	id: str = fields.UUIDField(pk=True)
	name: str = fields.CharField(max_length=40)
	inn: str = fields.CharField(max_length=12)
	signatory: str = fields.CharField(max_length=40)

	def __str__(self):
		return "suppliers = " + self.name

	# Класс для определения дополнительных настроек модели
	class Meta:
		# Имя таблицы в БД
		table = "suppliers"

	@staticmethod
	async def create(supplier_in: dict):
		supplier = SupplierDb(
			name=supplier_in["name"],
			inn=supplier_in["inn"],
			signatory=supplier_in["signatory"],
		)
		await supplier.save()
		return supplier