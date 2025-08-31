from fastapi import FastAPI
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="User Wallet API",
    description="An API for managing user wallets and transactions.",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the User Wallet API!"}