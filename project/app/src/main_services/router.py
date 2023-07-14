from fastapi import APIRouter, HTTPException

router = APIRouter(
	prefix="/main-services",
	tags=["Main-services"],
)
