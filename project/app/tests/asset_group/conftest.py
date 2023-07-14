import json

import pytest

from project.app.tests.utils import generate_random_string


#
# assets groups tests
#
@pytest.fixture
def asset_group_in():
	asset_group_in = {
		"type": "FIXED_ASSET",
		"short_name": generate_random_string(8),
		"full_name": generate_random_string(8)
	}
	return asset_group_in


@pytest.fixture
def updated_asset_group_in():
	updated_asset_group_in = {
		"type": "FIXED_ASSET",
		"short_name": "UPDATED" + generate_random_string(8),
		"full_name": "UPDATED" + generate_random_string(8)
	}
	return updated_asset_group_in


@pytest.fixture
def asset_group_out():
	def _asset_group_out(asset_group_id, asset_group_params):
		return dict({
			"id": asset_group_id,
			"type": "FIXED_ASSET",
			**asset_group_params,
			"amount_remains_in_storage": 0,
			"amount_in_use": 0,
			"is_active": True,
			"is_archived": False,
			"can_be_edited": True
		})

	return _asset_group_out


@pytest.fixture
def deleted_asset_group_out():
	def _deleted_asset_group_out(asset_group_id, asset_group_params):
		return dict({
			"id": asset_group_id,
			"type": "FIXED_ASSET",
			**asset_group_params,
			"amount_remains_in_storage": 0,
			"amount_in_use": 0,
			"is_active": True,
			"is_archived": True,
			"can_be_edited": False
		})

	return _deleted_asset_group_out


@pytest.fixture
def create_new_asset_group(test_app_with_db, asset_group_in):
	new_asset_group = test_app_with_db.post("/assets-groups/", content=json.dumps(asset_group_in))
	return new_asset_group.json()
