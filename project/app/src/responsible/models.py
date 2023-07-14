from tortoise import fields

from project.app.src.common.models import MyAbstractBaseModel
from project.app.src.common.models import ObjectStatusMixin
from project.app.src.common.models import TimestampMixin


class ResponsibleDb(MyAbstractBaseModel, ObjectStatusMixin, TimestampMixin):
	id = fields.UUIDField(pk=True)
	name = fields.CharField(null=False, max_length=20)
	surname = fields.CharField(null=False, max_length=20)
	patronymic = fields.CharField(null=True, max_length=20)
	employee_id = fields.CharField(null=True, max_length=5)

	def __str__(self):
		return "responsible_id = " + self.employee_id

	# Класс для определения дополнительных настроек модели
	class Meta:
		# Имя таблицы в БД
		table = "responsibles"

	@staticmethod
	async def create(responsible_in: dict):
		responsible = ResponsibleDb(
			name=responsible_in["name"],
			surname=responsible_in["surname"],
			patronymic=responsible_in["patronymic"],
			employee_id=responsible_in["employee_id"]
		)
		await responsible.save()
		return responsible
