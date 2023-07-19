# app.py
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

from views import home, about
# Router für die Home-View hinzufügen
app.include_router(home.router)

# Router für die About-View hinzufügen
app.include_router(about.router)
