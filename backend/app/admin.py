from fastapi import APIRouter, Request, HTTPException, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from .db import get_session
from .models import User, Wallet, Transaction
from .config import settings
from sqlmodel import select

router = APIRouter()

def check_admin(token: str | None):
    if token != settings.ADMIN_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")

@router.get('/', response_class=HTMLResponse)
def admin_index(token: str | None = None):
    check_admin(token)
    with next(get_session()) as session:
        users = session.exec(select(User)).all()
        wallets = session.exec(select(Wallet)).all()
        txs = session.exec(select(Transaction)).all()
    html = '<html><body><h1>TEOS Admin</h1>'
    html += '<h2>Users</h2><ul>' + ''.join([f'<li>{u.id} - {u.email} - {u.full_name}</li>' for u in users]) + '</ul>'
    html += '<h2>Wallets</h2><ul>' + ''.join([f'<li>{w.id} - {w.name} - {w.balance} {w.currency}</li>' for w in wallets]) + '</ul>'
    html += '<h2>Transactions</h2><ul>' + ''.join([f'<li>{t.id} - {t.amount} - {t.to_address} - {t.timestamp}</li>' for t in txs]) + '</ul>'
    html += '</body></html>'
    return HTMLResponse(html)

@router.post('/credit')
def admin_credit(wallet_id: int = Form(...), amount: float = Form(...), token: str | None = None):
    check_admin(token)
    with next(get_session()) as session:
        wallet = session.get(Wallet, wallet_id)
        if not wallet:
            raise HTTPException(404, 'wallet not found')
        wallet.balance += amount
        session.add(wallet); session.commit(); session.refresh(wallet)
    return RedirectResponse(url=f"/admin?token={token}", status_code=303)