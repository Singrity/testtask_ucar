from fastapi import APIRouter, Request
router = APIRouter()

@router.post("/create_incident")
async def create_incident():
