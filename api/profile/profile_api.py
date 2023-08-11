from main import app
from .profile_models import UserDent, CardDent
from fastapi import Body
# регистрация пользователя
@app.post("/api/register_user")
async def user_registration(user_data: UserDent):
    print(user_data)
    # после регистрации выдать айди пользователя
    return {"status": 1, "message": "Registration completed"}
# Вход в аккаунт
@app.post("/api/login-user")
async def login_user(phone_number: int =Body(), password: str = Body()):
    # проверка данных
    print(phone_number, password)
    checker = None
    # если данные верны, отправляем юзер айди
    return {"status": 1, "message": "Logged in"}

# Добавление карты в базу
@app.post("/api/add-card")
async def add_user_card(card_data: CardDent):
    # вызов функции из бд для добавления карты в базу
    result = card_data
    print(card_data)
    return {"status": 1, "message": result}
# вывод данных о пользователе
@app.get("/api/user_data")
async def get_user_data(user_id: int):
    pass
# вывод всех или определенных карт пользователя
@app.get("/api/user-cards")
async def get_user_card(user_id: int, card_id: int = 0):
    pass
