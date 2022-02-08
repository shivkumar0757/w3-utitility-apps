import requests
import time
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from staking_status_app.st_pool_status import get_staking_data
from staking_status_app.email import Emails

sched = BlockingScheduler()
logdata=[]
emdata=[]
counter = 0
#@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)

@sched.scheduled_job('interval', minutes=1)
def my_scheduled_job():
    global counter
    print('-------------------- Executed scheduled job @', datetime.datetime.now())
    em , log = get_staking_data()
    logdata.append(log)
    emdata.append(em)
    if counter < 5:
        print('email data: ')
        print(emdata)
        print('log data')
        print(logdata)
        counter += 1
    requests.get('https://w3-apps.herokuapp.com/')

@sched.scheduled_job('interval', minutes=120)
def doMail():
    send_email()

@sched.scheduled_job('cron', hour=5)
def send_email():
    data = f'''email data:
    {emdata}
===================================================================
    log data:
    {logdata}
    '''
    print('---------------------------------------Email Sending__________________________')
    Emails.sendMail('shivkumar0757@gmail.com',data )
    print('---------------------------------------Email Sending__________________________')


sched.start()