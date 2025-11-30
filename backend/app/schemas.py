from typing import Optional, List
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None

class UserRead(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str] = None

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class WalletCreate(BaseModel):
    name: str
    currency: Optional[str] = "TEOS"

class WalletRead(BaseModel):
    id: int
    name: str
    currency: str
    balance: float

class TransactionCreate(BaseModel):
    amount: float
    to_address: str
    memo: Optional[str] = None