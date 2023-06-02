import os


TORTOISE_ORM = {
	"connections": {"default": os.environ.get("DATABASE_URL")},
	"apps": {
		"models": {
			"models": [
				"project.app.src.asset_group.models",
				"project.app.src.responsible.models",
				"aerich.models"],
			"default_connection": "default",
		},
	},
}