from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    birthdate = Column(DateTime, nullable=False)
    gender = Column(String, nullable=False)
    telephone = Column(String, unique=True, nullable=False)
    adress = Column(String, nullable=False)
    city = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    country = Column(String, nullable=False)
    job = Column(String)
    company = Column(String)
    hobbies = Column(String)
    language = Column(String)
    topics = Column(String)
    notifications = Column(String)
    password = Column(String, nullable=False)
    consent = Column(Boolean, nullable=False)

    bookings = relationship("Booking", back_populates="user")

class Booking(Base):
    __tablename__ = "booking"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fk_user_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String, nullable=False)
    departure_date = Column(DateTime, nullable=False)
    return_date = Column(DateTime, nullable=False)
    departure_city = Column(String, nullable=False)
    arrival_city = Column(String, nullable=False)
    activities = Column(String)

    user = relationship("User", back_populates="bookings")
