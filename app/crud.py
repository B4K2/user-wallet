from sqlalchemy.orm import Session, joinedload
from . import models



def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    Fetch all users from the database with their associated wallets.
    - skip: for pagination, number of records to skip.
    - limit: for pagination, max number of records to return.
    """
    return db.query(models.User).options(joinedload(models.User.wallet)).offset(skip).limit(limit).all()