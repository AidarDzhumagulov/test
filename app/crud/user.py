from logger import logger
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from passlib.context import CryptContext

from models import user_models
from schemas.user_schema import UserCreate, UserUpdate


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserCrud:
    @classmethod
    def get_password_hash(cls, password: str):
        return pwd_context.hash(password)

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)

    # To get user by id from DB
    async def get_user_by_id(self, user_id: int, db: AsyncSession):
        stmt = select(user_models.User).filter(user_models.User.id == user_id)
        result = await db.execute(stmt)

        return result.scalar()

    # To get user by username from DB
    async def get_user_by_username(self, username: str, db: AsyncSession):
        stmt = select(user_models.User).filter(user_models.User.username == username)
        result = await db.execute(stmt)

        return result.scalar()

    # To create user by username and password into DB
    async def create_user(self, user: UserCreate, db: AsyncSession):
        hashed_password = self.get_password_hash(user.password)
        user = user_models.User(username=user.username, password=hashed_password)
        db.add(user)
        await db.commit()
        await db.refresh(user)
        logger.info(f"User id = {user.id} successfully created, username = {user.username}")
        return user

    # To update user by username in DB
    async def update_user_by_username(self, user: UserUpdate, username: str, db: AsyncSession):
        stmt = select(user_models.User).filter(user_models.User.username == username)
        result = await db.execute(stmt)
        db_user = result.scalar()
        logString = f'User id = {db_user.id} updated, '

        if user.full_name:
            logString += f'full_name (old = {db_user.full_name}, new = {user.full_name}), '
            db_user.full_name = user.full_name
        if user.sex:
            logString += f"sex (old = {db_user.sex}, new = {user.sex}) "
            db_user.sex = user.sex
        if user.birth_date:
            logString += f"birth_date (old = {db_user.birth_date}, new = {user.birth_date}) "
            db_user.birth_date = user.birth_date
        if user.address:
            logString += f"address (old = {db_user.address}, new = {user.address})"
            db_user.address = user.address

        db.add(db_user)
        await db.commit()
        logger.info(logString)
        return db_user

    # To delete user by username from DB
    async def delete_user_by_username(self, username: str, db: AsyncSession):
        stmt = select(user_models.User).filter(user_models.User.username == username)
        result = await db.execute(stmt)
        db_user = result.scalar()

        if db_user:
            await db.delete(db_user)
            await db.commit()
            logger.info(f"User = {username} successfully deleted!")
            return True
        return False
