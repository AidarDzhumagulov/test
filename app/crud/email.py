from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import email_models
from schemas.email_schema import EmailCreate, EmailUpdate


class EmailCrud:
    async def get_email_by_id(self, db: AsyncSession, email_id: int):
        stmt = select(email_models.Email).filter(email_models.Email.id == email_id)
        result = await db.execute(stmt)

        return result.scalar()

    async def create_email_user(self, db: AsyncSession, email: EmailCreate, user_id: int):
        email = email_models.Email(email=email.email, type_of_email=email.type_of_email, user_id=user_id)
        db.add(email)
        await db.commit()
        await db.refresh(email)
        return email

    async def update_email_by_id(self, db: AsyncSession, email: EmailUpdate, email_id: int):
        stmt = select(email_models.Email).filter(email_models.Email.id == email_id)
        result = await db.execute(stmt)
        db_email = result.scalar()

        if email.email:
            db_email.email = email.email
        if email.type_of_email:
            db_email.type_of_email = email.type_of_email
        if email.user_id:
            db_email.user_id = email.user_id

        db.add(db_email)
        await db.commit()
        return db_email

    async def delete_email_by_id(self, db: AsyncSession, email_id: int):
        stmt = select(email_models.Email).filter(email_models.Email.id == email_id)
        result = await db.execute(stmt)
        db_email = result.scalar()

        if db_email:
            await db.delete(db_email)
            await db.commit()
            return True
        return False
