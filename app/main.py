from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="User Wallet API",
    description="An API for managing user wallets and transactions.",
    version="1.0.0"
)

@app.post("/users/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_new_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, 
            detail="Email already registered"
        )
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of all users with their wallet information.
    """
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.post("/wallets/update/", response_model=schemas.Transaction)
def update_wallet(update_data: schemas.WalletUpdate, db: Session = Depends(get_db)):
    """
    Update a user's wallet balance by adding or subtracting an amount.
    A transaction record will be created for this operation.
    """
    db_transaction = crud.create_user_transaction(
        db=db, 
        user_id=update_data.user_id, 
        amount=update_data.amount
    )
    
    if db_transaction is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with id {update_data.user_id} not found"
        )
        
    return db_transaction

@app.get("/users/{user_id}/transactions/", response_model=list[schemas.Transaction])
def read_user_transactions(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve the full transaction history for a specific user.
    """
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with id {user_id} not found"
        )
    
    transactions = crud.get_user_transactions(db=db, user_id=user_id)
    return transactions


@app.get("/")
def read_root():
    return {"message": "Welcome to the User Wallet API!"}