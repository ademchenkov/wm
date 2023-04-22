import os

import pytest
from starlette.testclient import TestClient

from project.app.src.main import app
from project.app.src.config import Settings
from project.app.src.config import get_settings


def get_settings_override():
	return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope="module")
def test_app():
	# set up
	app.dependency_overrides[get_settings] = get_settings_override
	with TestClient(app) as test_client:
		# testing
		yield test_client

# tear down
