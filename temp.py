# from clock import send_email,emdata,logdata
from staking_status_app.email import Emails


print("-------------- Sending email-----------")

#send_email()
data = 'Testing email api'
Emails.sendMail('shivkumar0757@gmail.com',data )

print("email sent---------")

print('logData: ',send_email)

print('emdata: ', emdata)
