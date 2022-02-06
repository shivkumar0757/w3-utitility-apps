import requests
import time
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

#@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)

@sched.scheduled_job('interval', minutes=1)
def my_scheduled_job():
    print('-------------------- Executed')
    print(requests.post('https://cntr.click/b4jZyQ2'))
    with open('myfile.txt','a') as outf:
        outf.write(f'\n data!  : {datetime.datetime.now}' )
    

sched.start()