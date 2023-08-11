from pydantic import BaseModel
from datetime import datetime


class UserDent(BaseModel):
    profile_photo: str
    name: str
    surname: str
    phone_number: int
    email: str
    city: str
    reg_date: datetime

class CardDent(BaseModel):
    user_id: int
    card_number: int
    card_holder: str
    exp_date: int
    card_name: str
    card_balance: float
