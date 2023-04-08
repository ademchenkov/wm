def test_info(test_app):
	response = test_app.get("/")
	assert response.status_code == 200
	assert response.json() == {
		"app_name": "Warehouse Management",
		"environment": "test",
		"is_testing": True,
	}
