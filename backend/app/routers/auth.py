from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from ..models import User
from ..schemas import UserCreate, Token
from ..db import engine, get_session
from ..security import get_password_hash, verify_password, create_access_token

router = APIRouter()

@router.post("/register", response_model=dict)
def register(user: UserCreate):
    with Session(engine) as session:
        statement = select(User).where(User.email == user.email)
        res = session.exec(statement).first()
        if res:
            raise HTTPException(400, "Email already registered")
        db_user = User(email=user.email, full_name=user.full_name, hashed_password=get_password_hash(user.password))
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return {"id": db_user.id, "email": db_user.email}

@router.post("/login", response_model=Token)
def login(form: UserCreate):
    with Session(engine) as session:
        statement = select(User).where(User.email == form.email)
        user = session.exec(statement).first()
        if not user or not verify_password(form.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        token = create_access_token({"sub": str(user.id)})
        return {"access_token": token}