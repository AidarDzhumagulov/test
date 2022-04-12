from datetime import date
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserCreate(BaseModel):
    username: str
    password: str = Field(..., min_length=8)


class UserBase(BaseModel):
    username: str
    full_name: Optional[str]
    sex: Optional[str]
    birth_date: Optional[date]
    address: Optional[str]

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    full_name: Optional[str]
    sex: Optional[str]
    birth_date: Optional[date]
    address: Optional[str]

    class Config:
        orm_mode = True

# Кирова 23 офис 1 в 14:00 ( 7 апреля )