from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine
from . import models
from .routers import tarefas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="To-Do List API Simples")

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:5500",
    "null"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tarefas.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à To-Do List API Simples!"}