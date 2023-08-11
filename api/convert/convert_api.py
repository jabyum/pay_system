from main import app
import requests



@app.get('/api/get-currency')
async def get_rate():
    cb_api = requests.get('https://cbu.uz/ru/arkhiv-kursov-valyut/json/').json()
    usd_rate = cb_api[0]['Rate']
    eur_rate = cb_api[1]['Rate']
    rub_rate = cb_api[2]['Rate']

    return {'status': 1, 'rates': {'USD': usd_rate,
                                   'EUR': eur_rate,
                                   'RUB': rub_rate}}




