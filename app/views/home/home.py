# views/home.py
from fastapi import APIRouter, Request
from app import templates
import tensorflow as tf

router = APIRouter()

@router.get("/")
async def home(request: Request):
    array = ["Person 1", "Person 2", "Person 3", "Person 4"]
    context = {"request": request, "name": "Alice", "employee_array": array}
    return templates.TemplateResponse("index.html", context)