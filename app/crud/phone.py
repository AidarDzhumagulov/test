from sqlalchemy.orm import Session
from db.database import get_db
from models import user_models
from schemas.user_schema import PhoneCreate, PhoneUpdate


async def get_phone_by_id(db: Session, phone_id: int):
    return db.query(user_models.Phone).filter(user_models.Phone.id == phone_id).first()


def create_phone_user(db: Session, phone: PhoneCreate, user_id: int):
    db_phone = user_models.Phone(type_of_phone=phone.type_of_phone, number=phone.number, user_id=user_id)
    db.add(db_phone)
    db.commit()
    db.refresh(db_phone)
    return db_phone


async def update_phone_user(db: Session, phone: PhoneUpdate, phone_id: int):
    db_phone = db.query(user_models.Phone).filter(user_models.Phone.id == phone_id).first()

    if phone.number:
        db_phone.number = phone.number
    if phone.type_of_phone:
        db_phone.type_of_phone = phone.type_of_phone
    if phone.user_id:
        db_phone.user_id = phone.user_id

    db.add(db_phone)
    db.commit()
    return db_phone