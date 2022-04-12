from fastapi import APIRouter, Depends, HTTPException
from db.database import DbSession
from schemas.email_schema import EmailCreate, Email, EmailUpdate
from crud.email import EmailCrud



router = APIRouter()


@router.get("/{email_id}", tags=["Email"], response_model=Email)
async def get_user_email(email_id: int, email_crud: EmailCrud = Depends()):
    async with DbSession() as db:
        phone = await email_crud.get_email_by_id(db=db, email_id=email_id)
    return phone


@router.post("/{user_id}", tags=["Email"], response_model=Email)
async def create_email_for_user(user_id: int, email: EmailCreate, email_crud: EmailCrud = Depends()):
    async with DbSession() as db:
        return await email_crud.create_email_user(db=db, email=email, user_id=user_id)


@router.patch("/{email_id}", tags=["Email"], response_model=Email)
async def update_email_for_user(email_id: int, email: EmailUpdate, email_crud: EmailCrud = Depends()):
    async with DbSession() as db:
        update_phone = await email_crud.update_email_by_id(db, email, email_id)
        return update_phone


@router.delete("/{email_id}", tags=["Email"], response_model=str)
async def delete_email_by_id(email_id: int, email_crud: EmailCrud = Depends()):
    async with DbSession() as db:
        result = await email_crud.delete_email_by_id(email_id=email_id, db=db)
    if result:
        return f"Email successfully deleted"
    raise HTTPException(status_code=400, detail="Email not found")