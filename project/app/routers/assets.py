from fastapi import APIRouter

router = APIRouter()


@router.get("/assets")
def get_assets():
	pass


@router.post("/assets")
def create_asset():
	pass


@router.put("/assets/{asset-id}")
def update_asset():
	pass


@router.delete("/assets/{asset-id}")
def mark_as_unused_asset():
	pass