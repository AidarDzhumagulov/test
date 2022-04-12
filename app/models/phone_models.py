import enum
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from db.database import Base
from sqlalchemy.orm import relationship


class PhoneType(enum.Enum):
    MOBILE = "mobile"
    WORK = "work"


class Phone(Base):
    __tablename__ = "phones"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    type_of_phone = Column(Enum("mobile", "work", name="PhoneType"), default="work")
    number = Column(String, unique=True)

    user = relationship("User", backref="phones")
