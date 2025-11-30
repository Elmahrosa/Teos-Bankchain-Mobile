from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import init_db
from .routers import auth, users, wallets, transactions

app = FastAPI(title="TEOS BankChain API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(wallets.router, prefix="/wallets", tags=["wallets"])
app.include_router(transactions.router, prefix="/transactions", tags=["transactions"])

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def root():
    return {"service": "TEOS BankChain API", "status": "running"}