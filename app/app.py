# app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from starlette.responses import RedirectResponse

import subprocess
import os

import mlflow

from src.routes import basic

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


app.include_router(basic.router)
process = None

#Definition of Startup Events like the start of the mlflow dashboard and the corresponding environment variable.
#@app.on_event("startup")
#async def startup_event():
#    global process
#    print("FastAPI-Anwendung gestartet")
#    mlflow.set_tracking_uri('../../data/mlruns')
#    #os.environ["MLFLOW_TRACKING_URI"] = "./data/mlruns"
#    process = subprocess.Popen(["mlflow", "ui"], cwd="./data")
#    
#
#
## Stopping the mlflow dashboard after the backend server shutdown
#@app.on_event("shutdown")
#async def shutdown_event():
#    global process
#    print("FastAPI-Anwendung gestoppt")
#    if process is not None:
#        process.terminate()


#redirect for testing purposes and to have a look at the different routes that are set up.
@app.get('/')
def main():

    return RedirectResponse(url='/docs/')