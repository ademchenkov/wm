from project.app.exceptions.Exceptions import Exceptions

exceptions = Exceptions()
exceptions.add_exception("AssetGroup", "AG001", "Asset group not found")
exceptions.add_exception("AssetGroup", "AG002", "Cannot update asset group")
