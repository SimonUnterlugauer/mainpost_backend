# views/about.py
from fastapi import APIRouter, Request
from app import templates

router = APIRouter()

@router.get("/about")
async def about(request: Request):
    array = ["Person 1", "Person 2", "Person 3", "Person 4"]
    context = {"request": request, "name": "Gunnni", "employee_array": array}
    return templates.TemplateResponse("content/about.html", context)