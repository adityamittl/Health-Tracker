from django.db import models

# Create your models here.
from twilio.rest import Client

#defining a simple class
class Score(models.Model):
    #integer field
    test_result = models.PositiveIntegerField()

    #string representation
    def __str__(self):
        return str(self.test_result)

    #save method
    def save(self, *args, **kwargs):
        #if test_result is less than 80 execute this
        if self.test_result < 80:
            #twilio code
            account_sid = 'SK7408a1a9c65e8f94ac82d0f0eef4075e'
            auth_token = 'e1fadb1c019c793c4068c2c401f94d52'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                        body=f'Hi, your test result is {self.test_result}. Great job',
                                        from_='+17813325712',
                                        to='+91 99775 72889' 
                                    )

            print(message.sid)
        return super().save(*args, **kwargs)