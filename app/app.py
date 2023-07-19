# app.py
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
import tensorflow as tf

app = FastAPI()
templates = Jinja2Templates(directory="templates")

from logic.home import home
from logic.contentpages import about
# Router für die Home-View hinzufügen
app.include_router(home.router)

# Router für die About-View hinzufügen
app.include_router(about.router)
