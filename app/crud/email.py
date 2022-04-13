from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import email_models
from schemas.email_schema import EmailCreate, EmailUpdate
from logger import logger


class EmailCrud:
    """User's emails CRUD"""
    # To get user's email by id
    async def get_email_by_id(self, db: AsyncSession, email_id: int):
        stmt = select(email_models.Email).filter(email_models.Email.id == email_id)
        result = await db.execute(stmt)

        return result.scalar()

    # To create user's email by user_id
    async def create_email_user(self, db: AsyncSession, email: EmailCreate, user_id: int):
        email = email_models.Email(email=email.email, type_of_email=email.type_of_email, user_id=user_id)
        db.add(email)
        await db.commit()
        await db.refresh(email)
        logger.info(f"Email for user_id = {user_id} successfully created, email_id = {email.id}")
        return email

    # To update user's email by id
    async def update_email_by_id(self, db: AsyncSession, email: EmailUpdate, email_id: int):
        stmt = select(email_models.Email).filter(email_models.Email.id == email_id)
        result = await db.execute(stmt)
        db_email = result.scalar()
        logString = f"Email email_id = {email_id} updated "

        if email.email:
            logString += f'email (old = {db_email.email}, new = {email.email}), '
            db_email.email = email.email
        if email.type_of_email:
            logString += f'type of email (old = {db_email.type_of_email}, new = {email.type_of_email}), '
            db_email.type_of_email = email.type_of_email
        if email.user_id:
            logString += f'user_id (old = {db_email.user_id}, new = {email.user_id}),'
            db_email.user_id = email.user_id

        db.add(db_email)
        await db.commit()
        logger.info(logString)
        return db_email

    # To delete user's email by id
    async def delete_email_by_id(self, db: AsyncSession, email_id: int):
        stmt = select(email_models.Email).filter(email_models.Email.id == email_id)
        result = await db.execute(stmt)
        db_email = result.scalar()

        if db_email:
            await db.delete(db_email)
            await db.commit()
            logger.info(f"Email successfully deleted, phone_id = {email_id}")
            return True
        return False
