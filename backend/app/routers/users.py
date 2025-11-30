from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..models import User
from ..schemas import UserRead
from ..db import engine

router = APIRouter()

@router.get("/", response_model=list[UserRead])
def list_users():
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        return users