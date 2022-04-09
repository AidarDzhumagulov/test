import email
from fastapi import Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from db.database import get_db
from models import user_models
from schemas.user_schema import UserCreate, UserUpdate


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Auth:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    @classmethod
    def get_password_hash(cls, password: str):
        return pwd_context.hash(password)

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)

    async def get_user_by_id(self, user_id: int):
        return self.db.query(user_models.User).filter(user_models.User.id == user_id).first()

    async def get_user_by_username(self, username: str):
        return self.db.query(user_models.User).filter(user_models.User.username == username).first()

    async def get_user_by_email(self, email: str):
        return self.db.query(user_models.User).filter(user_models.Email.email == email).first()

    # async def get_users(self):
    #     users = self.db.query(user_models.User).all()
    #     res = []
    #     for user in users:
    #         res.append(user.to_json())
    #     return res

    def create_user(self, user: UserCreate):
        hashed_password = self.get_password_hash(user.password)
        user = user_models.User(username=user.username, password=hashed_password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return


    # def create_user(self, user: UserCreate):
    #     db_password = user_models.User(full_name=user.full_name,
    #                                    sex=user.sex,
    #                                    birth_date=user.birth_date,
    #                                    address=user.address)
    #     self.db.add(db_password)
    #     self.db.commit()
    #     self.db.refresh(db_password)
    #     return

    async def update_user_by_username(self, user: UserUpdate, username: str):
        db_user = self.db.query(user_models.User).filter(user_models.User.username == username).first()

        if user.full_name:
            db_user.full_name = user.full_name
        if user.sex:
            db_user.sex = user.sex
        if user.birth_date:
            db_user.birth_date = user.birth_date
        if user.address:
            db_user.address = user.address

        self.db.add(db_user)
        self.db.commit()
        return db_user

    # async def update_user_by_id(self, user: UserUpdate, user_id: int):
    #     user = self.db.query(user_models.User).filter(user_models.User.id == user_id).first()

    #     if user.full_name:
    #         user.full_name = user.full_name
    #     if user.sex:
    #         user.sex = user.sex
    #     if user.birth_date:
    #         user.birth_date = user.birth_date
    #     if user.address:
    #         user.address = user.address

    #     self.db.add(user)
    #     self.db.commit()
    #     return user

    async def delete_user_by_username(self, username: str):
        try:
            db_user = self.db.query(user_models.User).filter(user_models.User.username == username).first()
            self.db.delete(db_user)
            self.db.commit()
            return True
        except:
            return False
