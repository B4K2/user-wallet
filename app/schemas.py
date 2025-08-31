from pydantic import BaseModel, EmailStr
import datetime


class Wallet(BaseModel):
    id: int
    balance: float

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    name: str
    email: EmailStr  
    phone: str

class User(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    wallet: Wallet | None = None

    class Config:
        orm_mode = True

class WalletUpdate(BaseModel):
    user_id: int
    amount: float 

class TransactionBase(BaseModel):
    amount: float
    type: str

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    wallet_id: int
    timestamp: datetime.datetime

    class Config:
        orm_mode = True