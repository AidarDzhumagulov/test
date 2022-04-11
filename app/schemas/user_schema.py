from datetime import date
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class PhoneCreate(BaseModel):
    number: str
    type_of_phone: str


class PhoneUpdate(BaseModel):
    user_id: int
    number: str
    type_of_phone: str


class Phone(BaseModel):
    id: int
    user_id: int
    type_of_phone: str
    number: str

    class Config:
        orm_mode = True


class EmailCreate(BaseModel):
    type_of_email: str
    email: EmailStr


class EmailUpdate(BaseModel):
    user_id: int
    type_of_email: str
    email: EmailStr


class Email(BaseModel):
    id: int
    user_id: int
    type_of_email: str
    email: EmailStr

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    password: str = Field(..., min_length=8)


# class UserCreate(BaseModel):
#     full_name: Optional[str]
#     sex: str
#     birth_date: date
#     address: str


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