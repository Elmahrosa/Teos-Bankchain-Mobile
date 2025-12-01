from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter()
db = []  # demo; replace with persistent storage

class TokenIn(BaseModel):
    token: str
    user_id: int | None = None

@router.post('/register')
def register_token(payload: TokenIn):
    db.append(payload.dict())
    return {'registered': True, 'count': len(db)}