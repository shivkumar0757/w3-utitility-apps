import requests
import time
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from staking_status_app.st_pool_status import get_staking_data
from staking_status_app.email import Emails

sched = BlockingScheduler()
logdata=[]
emdata=[]

#@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)

@sched.scheduled_job('interval', minutes=5)
def my_scheduled_job():
    print('-------------------- Executed scheduled job @', datetime.datetime.now())
    log, em= get_staking_data()
    logdata.append(log)
    emdata.append(em)
    requests.get('https://w3-apps.herokuapp.com/')


@sched.scheduled_job('cron', hour=10)
def send_email():
    print('---------------------------------------Email Sending__________________________')
    Emails.sendMail('shivkumar0757@gmail.com',)
    print('---------------------------------------Email Sending__________________________')


sched.start()