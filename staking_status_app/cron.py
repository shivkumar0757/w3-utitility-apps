import requests

def my_scheduled_job():
    print('-------------------- Executed')
    print(requests.post('https://cntr.click/b4jZyQ2'))
    with open('myfile.txt','a') as outf:
        outf.write('data!')
    pass