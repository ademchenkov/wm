def test_get_app_info(test_app):
	response = test_app.get("/")
	assert response.status_code == 200
	assert response.json() == {
		"app_name": "Warehouse Management",
		"environment": "DEV",
		"is_testing": False
	}
