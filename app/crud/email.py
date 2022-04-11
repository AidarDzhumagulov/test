from sqlalchemy.orm import Session
from models import user_models
from schemas.user_schema import EmailCreate, EmailUpdate


async def get_email_by_id(db: Session, email_id: int):
    return db.query(user_models.Email).filter(user_models.Email.id == email_id).first()


def create_email_user(db: Session, em: EmailCreate, user_id: int):
    email = user_models.Email(email=em.email, type_of_email=em.type_of_email, user_id=user_id)
    db.add(email)
    db.commit()
    db.refresh(email)
    return email


async def update_email_by_id(db: Session, email: EmailUpdate, email_id: int):
    db_email = db.query(user_models.Email).filter(user_models.Email.id == email_id).first()

    if email.email:
        db_email.email = email.email
    if email.type_of_email:
        db_email.type_of_email = email.type_of_email
    if email.user_id:
        db_email.user_id = email.user_id

    db.add(db_email)
    db.commit()
    return db_email


async def delete_email_by_id(db: Session, email_id: int):
    try:
        db_user = db.query(user_models.Email).filter(user_models.Email.id == email_id).first()
        db.delete(db_user)
        db.commit()
        return True
    except:
        return False