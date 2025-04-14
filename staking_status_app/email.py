import smtplib

class Emails:
    def __init__(self):
        self.logId='mailtestdemoapi@gmail.com'
        self.logPass='XXX'
    
    def sendMail(self,reciever, msg):
        try:
            smtp = smtplib.SMTP('smtp.gmail.com', 587) 
            smtp.starttls() 
            #User Authentication 
            smtp.login(self.logId,self.logPass)

            #Sending the Email
            smtp.sendmail(self.logId, reciever,msg) 

            smtp.quit() 
            print ("Email sent successfully!") 
            return True
        except Exception as ex: 
            print("Something went wrong....",ex)
            
