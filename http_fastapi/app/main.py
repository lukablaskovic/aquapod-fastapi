from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from .db import engine, get_db
from .routers import aquapod, user, auth

from . import models

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:5173",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"msg": "FASTAPI REST API - Running ✅"}


app.include_router(aquapod.router)
app.include_router(user.router)
app.include_router(auth.router)
# Run with: uvicorn app.main:app --reload
