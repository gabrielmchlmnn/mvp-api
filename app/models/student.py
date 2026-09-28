from sqlalchemy import Column, Integer, String
from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    phone = Column(String(20), nullable=True)
    zip_code = Column(String(8), nullable=False)
