from pydantic import BaseModel, EmailStr


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