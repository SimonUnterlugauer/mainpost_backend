# app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Erlaube Zugriff von http://localhost:8080
origins = [
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from logic.employees import employees
from logic.home import home
# Router für die Home-View hinzufügen
app.include_route(remployees.router)
app.include_route(home.router)
app.include_route(to_frontend_test.router)

