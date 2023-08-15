from main import app
from .profile_models import UserDent, CardDent
from fastapi import Body
from database import profile_service
@app.post('/api/register-user')
async def user_registration(user_data: UserDent):
    checker = profile_service.phone_number(user_data.phone_number)
    if checker:
        return {"status": 0, "message": "Номер уже зарегистрирован"}
    profile_service.register_user_db(user_data)
    return {'status': 1, 'message': 'Registration completed'}

@app.post('/api/login-user')
async def login_user(phone_number: int = Body, password: str = Body):
    check = profile_service.login(phone_number, password)
    if check:
        return {'status': 1, 'message': check}
    return {"status": 0, "message": "Неправильные данные"}
@app.post('/api/add-card')
async def add_user_card(card_data: CardDent):
    result = profile_service.add_card_user(card_data)
    return {'status': 1, 'message': result}

@app.get('/api/user-data')
async def get_user_data(user_id):
    result = profile_service.user_id_informations(user_id)
    if result:
        return {'status': 1, 'message': result}
    return {"status": 0, "message": "Пользователь не найден"}
@app.get('/api/user-cards')
async def get_user_cards(user_id: UserDent, card_id: CardDent):
    result = profile_service.get_all_or_exact_card_db(user_id, card_id)
    return {'status': 1, 'message': result}
