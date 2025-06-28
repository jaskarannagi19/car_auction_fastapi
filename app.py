# main.py
from fastapi import FastAPI
from sqlmodel import Session, select
from model.db import engine, init_db
from models import ChassisRange

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

@app.post("/add")
def add_range(data: ChassisRange):
    with Session(engine) as session:
        session.add(data)
        session.commit()
        session.refresh(data)
        return data

@app.get("/ranges")
def get_all():
    with Session(engine) as session:
        return session.exec(select(ChassisRange)).all()