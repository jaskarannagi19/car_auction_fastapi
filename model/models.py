# models.py
from sqlmodel import SQLModel, Field
from typing import Optional

class IsuzuMotors(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_full_name: str
    chassis_type: str
    start_number: int
    end_number: int
    remarks: Optional[str] = None

