import os


TORTOISE_ORM = {
	"connections": {"default": os.environ.get("DATABASE_URL")},
	"apps": {
		"models": {
			"models": [
				"project.app.models.tortoise.AssetGroupTortoise",
				"aerich.models"],
			"default_connection": "default",
		},
	},
}