# db.py
from sqlmodel import SQLModel, create_engine

DATABASE_URL = "postgresql://postgres:12345678@localhost:5432/cardata"
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)
