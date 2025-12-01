from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from ..models import Transaction, Wallet
from ..schemas import TransactionCreate
from ..db import engine

router = APIRouter()

@router.post("/", response_model=dict)
def create_transaction(payload: TransactionCreate, wallet_id: int):
    with Session(engine) as session:
        wallet = session.get(Wallet, wallet_id)
        if not wallet:
            raise HTTPException(404, "Wallet not found")
        if wallet.balance < payload.amount:
            raise HTTPException(400, "Insufficient funds")
        wallet.balance -= payload.amount
        tx = Transaction(amount=payload.amount, to_address=payload.to_address, from_address=None, memo=payload.memo, wallet_id=wallet_id)
        session.add(tx)
        session.add(wallet)
        session.commit()
        session.refresh(tx)
        return {"tx_id": tx.id, "status": "ok"}