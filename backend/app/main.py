# backend/app/main.py
from fastapi import FastAPI

app = FastAPI(title="TEOS Backend (health)")

@app.get("/health")
async def health():
    return {"status": "ok"}
