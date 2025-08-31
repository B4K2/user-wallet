from pydantic import BaseModel


class Wallet(BaseModel):
    id: int
    balance: float

    class Config:
        orm_mode = True

class User(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    wallet: Wallet | None = None

    class Config:
        orm_mode = True