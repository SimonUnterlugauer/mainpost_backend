# views/home.py
from fastapi import APIRouter, Request
from app import templates
import tensorflow as tf

router = APIRouter()

@router.get("/")
async def home(request: Request):
    array = ["Simon Unterlugauer", "Jens Spahn", "Günther Glück", "Raimund Kolber"]
    context = {"request": request, "name": "Alice", "employee_array": array}
    return templates.TemplateResponse("home/index.html", context)