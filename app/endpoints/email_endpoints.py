from webbrowser import get
from fastapi import APIRouter, Depends, HTTPException
from db.database import get_db
from sqlalchemy.orm import Session
from schemas.user_schema import EmailCreate, Email, EmailUpdate
from crud.email import create_email_user, get_email_by_id, update_email_by_id



router = APIRouter()


@router.get("/{email_id}", tags=['Email'], response_model=Email)
async def get_user_email(email_id: int, db: Session = Depends(get_db)):
    phone = await get_email_by_id(db, email_id=email_id)
    return phone


@router.post("/", tags=["Email"], response_model=Email)
async def create_email_for_user(user_id: int, email: EmailCreate, db: Session = Depends(get_db)):
    return create_email_user(db=db, em=email, user_id=user_id)


@router.patch("/{email_id}", tags=["Email"], response_model=Email)
async def update_email_for_user(email_id: int, email: EmailUpdate, db: Session = Depends(get_db)):
    update_phone = await update_email_by_id(db, email, email_id)
    return update_phone


@router.delete("/{email_id}", tags=["Email"], response_model=str)
async def delete_email_by_id(email_id: int, db: Session = Depends(get_db)):
    db_user = await delete_email_by_id(email_id=email_id, db=db)
    if db_user:
        delete_email_by_id(db, email_id)
        return f"Phone successfully deleted"
    raise HTTPException(status_code=400, detail="User not found")