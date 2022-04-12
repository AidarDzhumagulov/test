import enum
from sqlalchemy import Column, String, Integer,Enum, ForeignKey
from db.database import Base
from sqlalchemy.orm import relationship


class EmailType(enum.Enum):
    PRIVATE = "private"
    WORK = "work"


class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    type_of_email = Column(Enum("private", "work", name="EmailType"), default="work")
    email = Column(String, default=EmailType.WORK, unique=True)

    user = relationship("User", backref="emails")