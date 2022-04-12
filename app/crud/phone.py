from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import phone_models
from schemas.phone_schema import PhoneCreate, PhoneUpdate

class PhoneCrud:
    async def get_phone_by_id(self, db: AsyncSession, phone_id: int):
        stmt = select(phone_models.Phone).filter(phone_models.Phone.id == phone_id)
        result = await db.execute(stmt)

        return result.scalar()

    async def create_phone_user(self, db: AsyncSession, phone: PhoneCreate, user_id: int):
        phone = phone_models.Phone(type_of_phone=phone.type_of_phone, number=phone.number, user_id=user_id)
        db.add(phone)
        await db.commit()
        await db.refresh(phone)
        return phone

    async def update_phone_user(self, db: AsyncSession, phone: PhoneUpdate, phone_id: int):
        stmt = select(phone_models.Phone).filter(phone_models.Phone.id == phone_id)
        result = await db.execute(stmt)
        db_phone = result.scalar()

        if phone.number:
            db_phone.number = phone.number
        if phone.type_of_phone:
            db_phone.type_of_phone = phone.type_of_phone
        if phone.user_id:
            db_phone.user_id = phone.user_id

        db.add(db_phone)
        await db.commit()
        return db_phone

    async def delete_phone_by_id(self, db: AsyncSession, phone_id: int):
        stmt = select(phone_models.Phone).filter(phone_models.Phone.id == phone_id)
        result = await db.execute(stmt)
        db_phone = result.scalar()

        if db_phone:
            await db.delete(db_phone)
            await db.commit()
            return True
        return False