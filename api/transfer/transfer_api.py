from main import app
from .transfer_models import P2PDent

@app.post('/api/transfer-money')
async def money_transfer(transfer_data: P2PDent):
    result = transfer_data
    print(result)
    return {'status': 1, 'message': result}

@app.get('/app/monitoring')
async def user_payments(user_id: int):
    pass
