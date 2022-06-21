from fastapi import FastAPI
from database.db import create_db

app = FastAPI(title="SQL Alchemy Crud", version="1.0.0")

@app.on_event("startup")
def startup():
    print("Startup")
    create_db()

@app.get("/")
def root():
    return {"message": "Hello World"}

    