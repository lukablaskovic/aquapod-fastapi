# aquapod-fastapi

*AquaPod* is an innovative project designed to address marine pollution by autonomously collecting waste from the sea. This repository hosts the code for the REST API built using *FastAPI*, used to control the AquaPod, as well as fetch sensor and other relevant data.

Install all the modules first:
```
pip install -r requirements.txt
```

To run the API:
```
uvicorn main:app --reload
```
Environment variables:
Linux, macOS, Windows Bash
```
export UVICORN_USER = "fill_me"
export UVICORN_PASSWORD = "fill_me"
export UVICORN_HOST = "fill_me"
export UVICORN_DATABASE = "aquapod"
```
For Windows Powershell, do:
```
$Env:UVICORN_USER = "fill_me"
...
```
