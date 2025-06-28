from sqlmodel import create_engine

# Change this to match your PostgreSQL connection string
DATABASE_URL = "postgresql://postgres:12345678@localhost:5432/cardata"

engine = create_engine(DATABASE_URL, echo=True)