from logger import logger
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import phone_models
from schemas.phone_schema import PhoneCreate, PhoneUpdate


class PhoneCrud:
    """User's Phone CRUD"""
    # To get user's phone by id from DB
    async def get_phone_by_id(self, db: AsyncSession, phone_id: int):
        stmt = select(phone_models.Phone).filter(phone_models.Phone.id == phone_id)
        result = await db.execute(stmt)

        return result.scalar()

    # To create user's phone into DB
    async def create_phone_user(self, db: AsyncSession, phone: PhoneCreate, user_id: int):
        phone = phone_models.Phone(type_of_phone=phone.type_of_phone, number=phone.number, user_id=user_id)
        db.add(phone)
        await db.commit()
        await db.refresh(phone)
        logger.info(f"Phone for user_id = {user_id} successfully created, phone_id = {phone.id}")
        return phone

    # To update user's phone by user_id in DB
    async def update_phone_user(self, db: AsyncSession, phone: PhoneUpdate, phone_id: int):
        stmt = select(phone_models.Phone).filter(phone_models.Phone.id == phone_id)
        result = await db.execute(stmt)
        db_phone = result.scalar()
        logString = f"Phone phone_id = {phone_id} updated "

        if phone.number:
            logString += f'phone number (old = {db_phone.number}, new = {phone.number}), '
            db_phone.number = phone.number
        if phone.type_of_phone:
            logString += f'type of phone (old = {db_phone.type_of_phone}, new = {phone.type_of_phone}), '
            db_phone.type_of_phone = phone.type_of_phone
        if phone.user_id:
            logString += f'user_id (old = {db_phone.user_id}, new = {phone.user_id}),'
            db_phone.user_id = phone.user_id

        db.add(db_phone)
        await db.commit()
        logger.info(logString)
        return db_phone

    # To delete user's phone by id from DB
    async def delete_phone_by_id(self, db: AsyncSession, phone_id: int):
        stmt = select(phone_models.Phone).filter(phone_models.Phone.id == phone_id)
        result = await db.execute(stmt)
        db_phone = result.scalar()

        if db_phone:
            await db.delete(db_phone)
            await db.commit()
            logger.info(f"Phone successfully deleted, phone_id = {phone_id}")
            return True
        return False
