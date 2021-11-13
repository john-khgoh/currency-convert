from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder

app = FastAPI()

rate = {
    'usd' : {'usd':1.0,'eur':0.87,'jpy':113.93},
    'eur' : {'usd':1.15,'eur':1.0,'jpy':130.34},
    'jpy' : {'usd':0.0088,'eur':0.0077,'jpy':1.0}
}

@app.get('/convert/{currency}/{target_currency}/{input}')
def convert(currency:str,target_currency:str,input:float):
    
    #Convert input currency and target currency to lowercase
    currency = currency.lower()
    target_currency = target_currency.lower()
    
    currency_list = []
    target_currency_list = []
    
    #Check that input currency rate is available, else raise HTTPException
    for _ in rate:
        currency_list.append(_)
    try:
        currency_list.index(currency)
    except:
        raise HTTPException(status_code=404, detail='%s not in currency list' %currency)
    
    #Check that target currency rate is available, else raise HTTPException
    for _ in rate[currency]:
        target_currency_list.append(_)
    try:
        target_currency_list.index(target_currency)
    except:
        raise HTTPException(status_code=404, detail='%s not in target currency list' %target_currency)
        
    value = input * rate[currency][target_currency]
    return {'value':'{:.2f}'.format(value),'currency':target_currency.upper()}