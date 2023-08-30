import os


TORTOISE_ORM = {
	"connections": {"default": os.environ.get("DATABASE_URL")},
	"apps": {
		"models": {
			"models": [
				"project.app.src.asset_group.models",
				"project.app.src.responsibles.models",
				"project.app.src.storages.models",
				"project.app.src.workplaces.models",
				"project.app.src.operations.models",
				"project.app.src.assets.models",
				"project.app.src.suppliers.models",
				"aerich.models"],
			"default_connection": "default",
		},
	},
}