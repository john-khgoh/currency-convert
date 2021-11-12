from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder

app = FastAPI()

rate = {
    'usd' : {'usd':1.0,'eur':2.0,'jpy':3.0},
    'eur' : {'usd':4.0,'eur':1.0,'jpy':5.0},
    'jpy' : {'usd':6.0,'eur':7.0,'jpy':1.0}
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
    return {'value':'{:.2f}'.format(value),'currency':target_currency}