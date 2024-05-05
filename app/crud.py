from sqlalchemy.orm import Session
from .import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_password = user.password + "fakedpass"
    db_user = models.User(**user.dict(), password=fake_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Booking).offset(skip).limit(limit).all()

def create_user_booking(db: Session, booking: schemas.BookingCreate, user_id: int):
    db_booking = models.Booking(**booking.dict(), fk_user_id=user_id)
    db.add(db_booking)
    db.commit
    db.refresh(db_booking)
    return db_booking

#def get_user_activity(db: Session,)