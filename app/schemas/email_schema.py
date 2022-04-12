from pydantic import BaseModel,  EmailStr
from typing import Optional


class EmailCreate(BaseModel):
    type_of_email: str
    email: EmailStr


class EmailUpdate(BaseModel):
    user_id: Optional[int]
    type_of_email: Optional[str]
    email: Optional[EmailStr]


class Email(BaseModel):
    id: Optional[int]
    user_id: Optional[int]
    type_of_email: Optional[str]
    email: Optional[EmailStr]

    class Config:
        orm_mode = True