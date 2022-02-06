import requests as req
import json
import datetime
import time

base_url= 'https://www.binance.com/bapi/earn/v1/friendly/pos/union'
params = {'status':'ALL','asset':'axs'}

def get_staking_data():
    response = req.get(base_url,params=params)
    rr=json.loads(response.content)
    email_data=[]
    log_data=[]
    if len(rr['data'])>0:
        for asset in rr['data']:
            if len(asset['projects']) > 0:
                for proj in asset['projects']:

                    if not proj['sellOut']:
                        email_data.append({'asset': proj['asset']+' '+ proj['duration'],
                                          'available': not proj['sellOut'] ,
                                          'time':str(datetime.datetime.now())})
                    log_data.append({'asset': proj['asset']+' '+ proj['duration'],
                                          'available': not proj['sellOut'] ,
                                          'time':str(datetime.datetime.now())})
    return email_data,log_data

