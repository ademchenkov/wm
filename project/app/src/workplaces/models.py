from tortoise import fields

from project.app.src.common.models import MyAbstractBaseModel
from project.app.src.common.models import ObjectStatusMixin
from project.app.src.common.models import TimestampMixin
from project.app.src.workplaces.constants import ModelPrefix


class WorkplaceDb(MyAbstractBaseModel, ObjectStatusMixin, TimestampMixin):
	id: str = fields.CharField(pk=True, max_length=40)
	building: str = fields.CharField(null=False, max_length=20)
	floor: str = fields.CharField(null=False, max_length=2)
	room: str = fields.CharField(null=False, max_length=5)
	place: str = fields.CharField(null=True, max_length=2)

	def __str__(self):
		return "workplaces = " + self.id

	# Класс для определения дополнительных настроек модели
	class Meta:
		# Имя таблицы в БД
		table = "workplaces"

	# Генерация id с префиксом
	async def generate_id(self):
		prefix = ModelPrefix.WORKPLACE_PREFIX

		self.id = f"{prefix}.{self.building[:4]}.{self.floor}.{self.room}.{self.place}"

	# Создание экземпляра класса со сгенерированным id
	@staticmethod
	async def create_with_id(building: str, floor: str, room: str, place: str | None):
		test_model = WorkplaceDb(
			building=building,
			floor=floor,
			room=room,
			place=place,
		)
		await test_model.generate_id()
		await test_model.save()
		return test_model
