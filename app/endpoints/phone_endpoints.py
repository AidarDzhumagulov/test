from fastapi import APIRouter, Depends, HTTPException
from crud.phone import PhoneCrud
from db.database import DbSession
from schemas.phone_schema import Phone, PhoneCreate, PhoneUpdate


router = APIRouter()


@router.get("/{phone_id}", tags=['Phone'], response_model=Phone)
async def get_user_phone(phone_id: int, phone_crud: PhoneCrud = Depends()):
    async with DbSession() as db:
        db_phone = await phone_crud.get_phone_by_id(db, phone_id)
    return db_phone


@router.post("/{user_id}", tags=['Phone'], response_model=Phone)
async def create_phone_for_user(user_id: int, phone: PhoneCreate, phone_crud: PhoneCrud = Depends()):
    async with DbSession() as db:
        return await phone_crud.create_phone_user(db=db, phone=phone, user_id=user_id)


@router.patch("/{phone_id}", tags=['Phone'], response_model=Phone)
async def update_phone_for_user(phone_id: int, phone: PhoneUpdate, phone_crud: PhoneCrud = Depends()):
    async with DbSession() as db:
        update_phone = await phone_crud.update_phone_user(db, phone, phone_id)
        return update_phone


@router.delete("/{phone_id}", tags=['Phone'], response_model=str)
async def delete_phone_by_(phone_id: int, phone_crud: PhoneCrud = Depends()):
    async with DbSession() as db:
        result = await phone_crud.delete_phone_by_id(db=db, phone_id=phone_id)
    if result:
        return f"Phone successfully deleted"
    raise HTTPException(status_code=400, detail="Phone not found")
