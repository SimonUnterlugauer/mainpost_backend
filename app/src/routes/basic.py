from fastapi import APIRouter, Depends
from starlette.responses import RedirectResponse

import pandas as pd
import numpy as np
import json


#All Routes will be passed by the prefix /model
router = APIRouter(
    prefix="/basic",
    tags=["basic"]
)


#Function to beautify the json output that is generated by the pandas dataframes
def df_to_json(df):
    res = df.to_json(orient="records")
    parsed = json.loads(res)
    return parsed

@router.get('/employee_data')
async def employee_data():
    df = pd.read_csv('./data/processed/absences_daily.csv')
    return df_to_json(df)

@router.get('/emp')
async def employee_data():
    df = pd.read_csv('./data/processed/absences_daily.csv')
    return df_to_json(df)
