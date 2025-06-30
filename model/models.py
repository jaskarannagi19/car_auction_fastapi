# models.py
from sqlmodel import SQLModel, Field
from typing import Optional

class IsuzuMotors(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_full_name: str
    chassis_type: str
    start_number: int
    end_number: int
    year: int=Field(default=1000)
    remarks: Optional[str] = None

class UDTrucks(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_full_name: str
    chassis_type: str
    start_number: int
    end_number: int
    year: int=Field(default=1000)
    remarks: Optional[str] = None

class YamahaMotor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_full_name: str
    chassis_type: str
    start_number: int
    end_number: int
    year: int=Field(default=1000)
    remarks: Optional[str] = None

class MitsubishiFusoTruckandBusCorporation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_full_name: str
    chassis_type: str
    start_number: int
    end_number: int
    year: int=Field(default=1000)
    remarks: Optional[str] = None

class MitsubishiMotors(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_full_name: str
    chassis_type: str
    start_number: int
    end_number: int
    year: int=Field(default=1000)
    remarks: Optional[str] = None


class MazdaMotorCorporation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_full_name: str
    chassis_type: str
    start_number: int
    end_number: int
    year: int=Field(default=1000)
    remarks: Optional[str] = None

class HondaMotor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_full_name: str
    chassis_type: str
    start_number: int
    end_number: int
    year: int=Field(default=1000)
    remarks: Optional[str] = None


class HinoMotorsCorporation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_full_name: str
    chassis_type: str
    start_number: int
    end_number: int
    year: int=Field(default=1000)
    remarks: Optional[str] = None


class NissanMotor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_full_name: str
    chassis_type: str
    start_number: int
    end_number: int
    year: int=Field(default=1000)
    remarks: Optional[str] = None

class ToyotaMotorCorporation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_full_name: str
    chassis_type: str
    start_number: int
    end_number: int
    year: int=Field(default=1000)
    remarks: Optional[str] = None

class DaihatsuMotorCorporation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_full_name: str
    chassis_type: str
    start_number: int
    end_number: int
    year: int=Field(default=1000)
    remarks: Optional[str] = None

class SubaruCorporation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_full_name: str
    chassis_type: str
    start_number: int
    end_number: int
    year: int=Field(default=1000)
    remarks: Optional[str] = None

class SuzukiMotorCorporation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_full_name: str
    chassis_type: str
    start_number: int
    end_number: int
    year: int=Field(default=1000)
    remarks: Optional[str] = None


class KawasakiMotorsCorporation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    model_full_name: str
    chassis_type: str
    start_number: int
    end_number: int
    year: int=Field(default=1000)
    remarks: Optional[str] = None

