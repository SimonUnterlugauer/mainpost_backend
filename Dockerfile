# Verwenden Sie das Python-Basisimage
FROM python:3.9

# Arbeitsverzeichnis im Container festlegen
WORKDIR /app

# Erstellen Sie eine virtuelle Umgebung
RUN python -m venv /venv

# Aktivieren Sie die virtuelle Umgebung
ENV PATH="/venv/bin:$PATH"

# Kopieren Sie die Anwendungsdateien in das Arbeitsverzeichnis im Container
COPY ./app/app.py /app/app.py
# Kopieren Sie die package.json und package-lock.json in das Arbeitsverzeichnis im Container
COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json

# Installieren der erforderlichen python Abhängigkeiten
COPY requirements.txt /app/requirements.txt

# Installieren Sie die erforderlichen npm-Abhängigkeiten
#RUN apt-get update && apt-get install -y npm
#RUN npm install 

# Installieren Sie die erforderlichen Python-Abhängigkeiten
RUN pip install -r /app/requirements.txt

# Starten Sie die FastAPI-Anwendung mit Uvicorn und aktivieren Sie das Live-Reload
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

