# Verwenden Sie das Python-Basisimage
FROM python:3.9

# Arbeitsverzeichnis im Container festlegen
WORKDIR /app

# Kopieren Sie die Anwendungsdateien in das Arbeitsverzeichnis im Container
COPY ./app.py /app/app.py

# Installieren Sie die erforderlichen Python-Abhängigkeiten
RUN pip install fastapi uvicorn

# Starten Sie die FastAPI-Anwendung mit Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
