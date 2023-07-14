import json


# happy pass tests

def test_create_asset_group(test_app_with_db, asset_group_in, asset_group_out):
	response = test_app_with_db.post("/assets-groups/", content=json.dumps(asset_group_in))

	result = asset_group_out(response.json()["id"], asset_group_in)
	assert response.status_code == 201
	assert response.json() == result


def test_get_all_asset_groups(test_app_with_db):
	response = test_app_with_db.get("/assets-groups/")

	assert response.status_code == 200
	assert response.json() is not None


def test_get_asset_group_by_id(test_app_with_db, create_new_asset_group, asset_group_in, asset_group_out):
	new_asset_group_id = create_new_asset_group["id"]
	response = test_app_with_db.get("/assets-groups/" + new_asset_group_id)

	result = asset_group_out(new_asset_group_id, asset_group_in)

	assert response.status_code == 200
	assert response.json() == result


def test_update_asset_group(test_app_with_db, create_new_asset_group, updated_asset_group_in, asset_group_out):
	new_asset_group_id = create_new_asset_group["id"]
	updated_asset_group_in_json = updated_asset_group_in

	response = test_app_with_db.patch(
		"/assets-groups/" + new_asset_group_id,
		content=json.dumps(updated_asset_group_in_json)
	)

	result = asset_group_out(new_asset_group_id, updated_asset_group_in_json)

	assert response.status_code == 200
	assert response.json() == result


def test_delete_asset_group(test_app_with_db, create_new_asset_group, asset_group_in, deleted_asset_group_out):
	new_asset_group_id = create_new_asset_group["id"]

	response = test_app_with_db.delete(
		"/assets-groups/" + new_asset_group_id
	)

	result = deleted_asset_group_out(new_asset_group_id, asset_group_in)

	assert response.status_code == 200
	assert response.json() == result