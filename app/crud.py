from sqlalchemy.orm import Session, joinedload
from . import models, schemas



def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    Fetch all users from the database with their associated wallets.
    - skip: for pagination, number of records to skip.
    - limit: for pagination, max number of records to return.
    """
    return db.query(models.User).options(joinedload(models.User.wallet)).offset(skip).limit(limit).all()


def get_user_by_email(db: Session, email: str):
    """
    Fetch a single user by their email address.
    """
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    """
    Create a new user and an associated wallet in the database.
    """
    db_user = models.User(
        name=user.name,
        email=user.email,
        phone=user.phone
    )
    
    db_wallet = models.Wallet(
        balance=0.0,
        user=db_user  
    )
    
    db.add(db_user)
    db.add(db_wallet)
    
    db.commit()
    
    db.refresh(db_user)
    
    return db_user