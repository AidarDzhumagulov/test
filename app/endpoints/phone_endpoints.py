from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.user_schema import Phone, PhoneCreate, PhoneUpdate
from crud.phone import create_phone_user, get_phone_by_id, update_phone_user


router = APIRouter()



@router.get("/{phone_id}", tags=['Phone'], response_model=Phone)
async def get_user_phone(phone_id: int, db: Session = Depends(get_db)):
    phone = await get_phone_by_id(db, phone_id=phone_id)
    return phone


@router.post("/")
async def create_phone_for_user(user_id: int, phone: PhoneCreate, db: Session = Depends(get_db)):
    return create_phone_user(db=db, phone=phone, user_id=user_id)


@router.patch("/{phone_id}", tags=["phone"], response_model=Phone)
async def update_phone_for_user(phone_id: int, phone: PhoneUpdate, db: Session = Depends(get_db)):
    update_phone = await update_phone_user(db, phone, phone_id)
    return update_phone


@router.delete("/")
async def delete_phone_by_():
    pass