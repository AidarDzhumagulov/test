from pydantic import BaseModel
from typing import Optional


class PhoneCreate(BaseModel):
    number: str
    type_of_phone: str


class PhoneUpdate(BaseModel):
    user_id: Optional[int]
    number: Optional[str]
    type_of_phone: Optional[str]


class Phone(BaseModel):
    id: Optional[int]
    user_id: Optional[int]
    type_of_phone: Optional[str]
    number: Optional[str]

    class Config:
        orm_mode = True
