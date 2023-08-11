from fastapi import Body
from database.profile_service import login_db, add_card_db, get_user_data_db
from main import app
from profile_models import UserDent, CardDent


@app.post('/api/register-user')
async def register_user(user_data: UserDent):
    print(user_data)

    return {'status': 1, 'message': 'Registration complete'}


@app.post('/api/login-user')
async def login_user(phone_number: int = Body(), password: str = Body()):
    checker = login_db(phone_number, password)
    if checker:
        return {'status': 1, 'message': 'Logged in'}
    return {'status': 0,'message': 'Invalid login'}

@app.post('/api/add-card')
async def add_user_card(card_data: CardDent):
    result = add_card_db(card_data.card_number, card_data.exp_date, card_data.card_name,
                         card_data.card_balance, card_data.user_id)

    if result:
        return {'status': 1, 'message': result}
    return {'status': 0,'message': 'Card not added'}
@app.get('/api/user-data')
async def get_user_data(user_id: int):
    exact_user = get_user_data_db(user_id)

    if exact_user:
        return {'status': 1, 'message': exact_user}
    return {'status': 0,'message': 'User not found'}

@app.get('/api/get-cards')
async def get_user_card(user_id: int, card_id: int = 0):
    pass

