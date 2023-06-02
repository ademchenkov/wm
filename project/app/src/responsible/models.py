from tortoise.models import Model
from tortoise import fields


class ResponsibleDb(Model):
	id = fields.UUIDField(pk=True)
	name = fields.CharField(null=False, max_length=20)
	surname = fields.CharField(null=False, max_length=20)
	patronymic = fields.CharField(null=True, max_length=20)
	employee_id = fields.CharField(null=True, max_length=5)
	is_active = fields.BooleanField(null=False, default=True)
	is_archived = fields.BooleanField(null=False, default=False)
	can_be_edited = fields.BooleanField(null=False, default=True)
	created_at = fields.DatetimeField(null=False, auto_now_add=True)
	updated_at = fields.DatetimeField(auto_now=True)

	def __str__(self):
		return "employee_id = " + self.employee_id

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
