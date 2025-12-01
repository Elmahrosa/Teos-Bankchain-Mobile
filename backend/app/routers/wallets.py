from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from ..models import Wallet, User
from ..schemas import WalletCreate, WalletRead
from ..db import engine

router = APIRouter()

@router.post("/", response_model=WalletRead)
def create_wallet(payload: WalletCreate):
    with Session(engine) as session:
        wallet = Wallet(name=payload.name, currency=payload.currency, balance=0.0)
        session.add(wallet)
        session.commit()
        session.refresh(wallet)
        return wallet

@router.get("/", response_model=list[WalletRead])
def list_wallets():
    with Session(engine) as session:
        wallets = session.exec(select(Wallet)).all()
        return wallets

@router.get("/{wallet_id}", response_model=WalletRead)
def get_wallet(wallet_id: int):
    with Session(engine) as session:
        wallet = session.get(Wallet, wallet_id)
        if not wallet:
            raise HTTPException(404, "Wallet not found")
        return wallet