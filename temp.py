from clock import send_email,emdata,logdata
from staking_status_app.email import Emails


print("-------------- Sending email-----------")

#send_email()
data = 'Testing email api'
em= Emails()
em.sendMail('shivkumar0757@gmail.com',data )

print("email sent---------")

print('logData: ',logdata)

print('emdata: ', emdata)
