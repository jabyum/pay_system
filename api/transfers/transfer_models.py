from pydantic import BaseModel
from datetime import datetime

# модель перевода с карты на карту
class P2PDent(BaseModel):
    card_from: int
    amount: float
    card_to: int
    transfer_time: datetime

