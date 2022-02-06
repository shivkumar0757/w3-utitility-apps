import requests
import time

def my_scheduled_job():
    print('-------------------- Executed')
    print(requests.post('https://cntr.click/b4jZyQ2'))
    with open('myfile.txt','a') as outf:
        outf.write(f'\n data!  : {time.datetime.now}' )
    pass

while True:
    print('------------------------ calling____________')
    my_scheduled_job()
    time.sleep(5)