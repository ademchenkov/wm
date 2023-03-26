from fastapi import APIRouter
from pydantic import UUID4

router = APIRouter()


@router.get("/assets")
async def get_assets():
	pass


@router.post("/assets")
def create_asset():
	pass


@router.put("/assets/{asset-id}")
def update_asset(asset_id: UUID4):
	pass


@router.delete("/assets/{asset-id}")
def mark_as_unused_asset(asset_id: UUID4):
	pass