from fastapi import APIRouter, HTTPException
import httpx
from ..config import settings

router = APIRouter()

EXPO_PUSH_URL = "https://exp.host/--/api/v2/push/send"

@router.post('/send')
async def send_push(token: str, title: str, body: str):
    message = {"to": token, "title": title, "body": body}
    async with httpx.AsyncClient() as client:
        r = await client.post(EXPO_PUSH_URL, json=message, timeout=10)
    if r.status_code != 200:
        raise HTTPException(500, "Expo push failed")
    return r.json()