from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="User Wallet API",
    description="An API for managing user wallets and transactions.",
    version="1.0.0"
)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of all users with their wallet information.
    """
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/")
def read_root():
    return {"message": "Welcome to the User Wallet API!"}