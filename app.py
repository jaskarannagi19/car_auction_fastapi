from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlmodel import Session, select
from model.models import IsuzuMotors, SQLModel
from db import engine  # assume you have a db.py with `engine` created

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.get("/get-model")
def get_model(number: int):
    with Session(engine) as session:
        result = session.exec(
            select(IsuzuMotors).where(
                IsuzuMotors.start_number <= number,
                IsuzuMotors.end_number >= number
            )
        ).first()
        return {"model": result.model_full_name if result else "Not found"}