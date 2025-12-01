from fastapi import APIRouter
from ..payments.pi import create_pi_payment

router = APIRouter()

@router.post('/pi')
def pi_pay(user_id:int, amount:float, memo:str|None=None):
    return create_pi_payment(user_id, amount, memo)