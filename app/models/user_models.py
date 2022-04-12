import enum
from sqlalchemy import Column, String, Integer, Date, Enum
from db.database import Base
from sqlalchemy.orm import relationship


class Gender(enum.Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class User(Base):
    __tablename__ = "users"

    # Register fields
    username = Column(String, unique=True)
    password = Column(String)

    # User data fields
    full_name = Column(String)
    # sex = Column(Enum(Gender))
    sex = Column(Enum("male", "female", "other", name="Gender"), default="male")
    birth_date = Column(Date)
    address = Column(String)

    # Status fields
    id = Column(Integer, primary_key=True, index=True)
