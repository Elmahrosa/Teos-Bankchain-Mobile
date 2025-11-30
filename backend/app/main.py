from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

from .db import init_db
from .routers import auth, users, wallets, transactions
from .admin import router as admin_router
from .routers import push, push_register, payments

# Rate limiter setup
limiter = Limiter(key_func=get_remote_address)

# FastAPI app instance
app = FastAPI(
    title="TEOS BankChain API",
    version="1.0.0",
    description="Bank-facing crypto gateway with civic-first Web3 infrastructure"
)
app.state.limiter = limiter
app.add_exception_handler(429, _rate_limit_exceeded_handler)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(wallets.router, prefix="/wallets", tags=["wallets"])
app.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
app.include_router(admin_router, prefix="/admin", tags=["admin"])
app.include_router(push.router, prefix="/push", tags=["push"])
app.include_router(push_register.router, prefix="/push", tags=["push-register"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])

# Startup hook
@app.on_event("startup")
def on_startup():
    init_db()

# NOTE:
# No /health endpoint anymore.
# Contributors should check http://127.0.0.1:8000/docs (Swagger UI)
# or http://127.0.0.1:8000/redoc (ReDoc) for API documentation.
