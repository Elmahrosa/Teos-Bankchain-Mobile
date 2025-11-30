# backend/src/main.py

from fastapi import FastAPI

app = FastAPI(
    title="TEOS BankChain Mobile API",
    description="Bank-facing crypto ↔ fiat gateway backend",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "TEOS BankChain Mobile API"
    }

