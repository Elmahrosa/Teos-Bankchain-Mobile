from ..config import settings
def create_pi_payment(user_id:int, amount:float, memo:str|None=None):
    # Placeholder: call Pi Network API in production with settings.PI_API_KEY
    return {
        "status": "created",
        "provider": "pi-stub",
        "amount": amount,
        "user_id": user_id,
        "memo": memo
    }