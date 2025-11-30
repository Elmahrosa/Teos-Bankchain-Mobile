from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from pydantic import EmailStr

class UserBase(SQLModel):
    email: EmailStr
    full_name: Optional[str] = None

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str
    wallets: list["Wallet"] = Relationship(back_populates="owner")

class WalletBase(SQLModel):
    name: str
    currency: str = "TEOS"

class Wallet(WalletBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    owner_id: Optional[int] = Field(default=None, foreign_key="user.id")
    balance: float = 0.0
    owner: Optional[User] = Relationship(back_populates="wallets")
    transactions: list["Transaction"] = Relationship(back_populates="wallet")

class TransactionBase(SQLModel):
    amount: float
    to_address: str
    from_address: Optional[str] = None
    memo: Optional[str] = None

class Transaction(TransactionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    wallet_id: Optional[int] = Field(default=None, foreign_key="wallet.id")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    wallet: Optional[Wallet] = Relationship(back_populates="transactions")