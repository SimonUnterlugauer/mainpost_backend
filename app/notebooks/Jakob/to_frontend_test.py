from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import pandas as pd

router = APIRouter()

async def absences_per_day():
    days_of_week = pd.read_csv("../../data/interim/absences_per_day.csv", delimiter=',')
    days_of_week = days_of_week[['day_of_week', 'count']]


@router.get("/absences_per_day_of_week")
async def home(request: Request):

    days_of_week = absences_per_day()
    return JSONResponse(content=days_of_week)








#async def machiwasmitdendaten():
#    return "Hallo"

#@router.get("/day_of_week")
#async def home(request: Request):

#    var = machiwasmitdendaten()

#    my_df = pd.read_csv("../../data/interim/absences_per_day.csv", delimiter=',')
#    my_df = my_df[['day_of_week', 'count']]

#    return JSONResponse(content=var)