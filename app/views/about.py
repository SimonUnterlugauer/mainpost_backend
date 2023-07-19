# views/about.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/about")
async def about():
    return {"message": "This is the about page!"}