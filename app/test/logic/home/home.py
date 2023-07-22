# views/home.py
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter()

employees_data = {
    "employees": [
    { "id": 1, "name": "Max Mustermann", "abteilung": "Vertrieb" },
    { "id": 2, "name": "Lisa Müller", "abteilung": "Marketing" },
    { "id": 3, "name": "Peter Schmidt", "abteilung": "Produktion" },
    { "id": 4, "name": "Sarah Wagner", "abteilung": "Personal" },
    { "id": 5, "name": "Michael Keller", "abteilung": "IT" },
    { "id": 6, "name": "Julia Weber", "abteilung": "Vertrieb" },
    { "id": 7, "name": "Andreas Becker", "abteilung": "Marketing" },
    { "id": 8, "name": "Carolin Hoffmann", "abteilung": "Personal" },
    { "id": 9, "name": "Christian Fischer", "abteilung": "IT" },
    { "id": 10, "name": "Anja Schneider", "abteilung": "Produktion" },
    { "id": 11, "name": "Markus Schulz", "abteilung": "IT" },
    { "id": 12, "name": "Petra Maier", "abteilung": "Personal" },
    { "id": 13, "name": "Thomas Wagner", "abteilung": "Vertrieb" },
    { "id": 14, "name": "Nina Keller", "abteilung": "Marketing" },
    { "id": 15, "name": "Felix Weber", "abteilung": "IT" },
    { "id": 16, "name": "Marie Hoffmann", "abteilung": "Personal" },
    { "id": 17, "name": "Alexandra Becker", "abteilung": "Produktion" },
    { "id": 18, "name": "Stefan Fischer", "abteilung": "IT" },
    { "id": 19, "name": "Laura Schneider", "abteilung": "Vertrieb" },
    { "id": 20, "name": "Jonas Schulz", "abteilung": "Marketing" },
    { "id": 21, "name": "Anna Maier", "abteilung": "Personal" },
    { "id": 22, "name": "David Wagner", "abteilung": "IT" },
    { "id": 23, "name": "Sophie Keller", "abteilung": "Produktion" },
    { "id": 24, "name": "Tim Weber", "abteilung": "IT" },
    { "id": 25, "name": "Lea Hoffmann", "abteilung": "Personal" },
    { "id": 26, "name": "Julian Becker", "abteilung": "Vertrieb" },
    { "id": 27, "name": "Hannah Fischer", "abteilung": "Marketing" },
    { "id": 28, "name": "Paul Maier", "abteilung": "Personal" },
    { "id": 29, "name": "Lena Schneider", "abteilung": "IT" },
    { "id": 30, "name": "Tom Schulz", "abteilung": "Produktion" }
  ]
}

@router.get("/employees")
async def home(request: Request):
    return JSONResponse(content=employees_data)