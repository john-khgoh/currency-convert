from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
import urllib3
import json

http = urllib3.PoolManager()
app = FastAPI()
url = 'http://api.currencylayer.com/live'
access_key ='a2f977ecb7d73dbb82f287eaab8f4666'
format = 1
source_url= url + '?' + 'access_key' + '=' + access_key + '&' + 'format' + '=' + str(format)

rate = {
    'usd' : {'usd':1.0,'eur':0.87,'jpy':113.93},
    'eur' : {'usd':1.15,'eur':1.0,'jpy':130.34},
    'jpy' : {'usd':0.0088,'eur':0.0077,'jpy':1.0}
}

#Updates the currency exchange rate from a publicly available service
@app.get('/update-rate')
def update_rate():
    try:    
        r = http.request('GET',source_url)
    except:
        raise HTTPException(status_code=502, detail='Unable to access data source server')
    
    new_rate = r.data.decode('ascii')
    new_rate = json.loads(new_rate)

    rate['usd']['eur'] = '{:.5f}'.format(new_rate['quotes']['USDEUR'] )
    rate['usd']['jpy'] = '{:.5f}'.format(new_rate['quotes']['USDJPY'])
    rate['eur']['usd'] = '{:.5f}'.format(1.0/(new_rate['quotes']['USDEUR']))
    rate['jpy']['usd'] = '{:.5f}'.format(1.0/(new_rate['quotes']['USDJPY']))
    rate['eur']['jpy'] = '{:.5f}'.format(float(rate['usd']['jpy'])/float(rate['usd']['eur']))
    rate['jpy']['eur'] = '{:.5f}'.format(1.0/float(rate['eur']['jpy']))
    
    return("Rate updated!")

#Convert from one currency to another
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
        
    value = input * float(rate[currency][target_currency])
    return {'value':'{:.2f}'.format(value),'currency':target_currency.upper()}