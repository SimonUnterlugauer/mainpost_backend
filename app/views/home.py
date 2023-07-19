# views/home.py
from fastapi import APIRouter, Request
from app import templates
import tensorflow as tf

router = APIRouter()

@router.get("/")
async def home(request: Request):
    context = {"request": request, "name": "Alice"}
    return templates.TemplateResponse("index.html", context)