from sqlalchemy import Column, String, Integer, Enum, Date, ForeignKey
from db.database import Base
from sqlalchemy.orm import relationship


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class PhoneType(Enum):
    MOBILE = "mobile"
    WORK = "work"


class EmailType(Enum):
    PRIVATE = "private"
    WORK = "work"


class User(Base):
    __tablename__ = "users"

    username = Column(String, unique=True)
    password = Column(String)
    full_name = Column(String)
    sex = Column(Enum("male", "female", "other", name="Gender"), default="male")
    birth_date = Column(Date)
    address = Column(String)


    #Status fields
    id = Column(Integer, primary_key=True, index=True)

    phone = relationship("Phone", backref="users")
    email = relationship("Email", backref="users")


class Phone(Base):
    __tablename__ = "phones"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    type_of_phone = Column(Enum("mobile", "work", name=PhoneType), default="work")
    number = Column(String, unique=True)

    user = relationship("User", backref="phones")


class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    type_of_email = Column(Enum("mobile", "work", name=EmailType), default="work")
    email = Column(String, default=EmailType.WORK, unique=True)

    user = relationship("User", backref="emails")
