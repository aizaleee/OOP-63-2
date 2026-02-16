import random


class UserAccount:
    def __init__(self, username, score, pin):
        self.username = username
        self._score = score
        self.__pin = pin

    def access(self, username, pin):
        if self.username == username and self.__pin == pin:
            return print( " you accessed you account")
        else:
            return print("please retry")
    

    def __random_pass(self):
        return random.randint(1, 10)
    

    def reset_pass(self, username):
        if username == self.username:
            self.__password = self.__random_pass()
        else:
            print("Error!!!")


    def get_score(self):
        return self._score
    

    def get_pin(self):
        return self.__pin

    
Aiz = UserAccount("Aiz", 1000, "1221122")
print(Aiz.get_score())
print(Aiz.get_pin())



from abc import ABC, abstractmethod

class NotificationService(ABC):


    @abstractmethod
    def send_to_phone(self):
        pass
    @abstractmethod
    def send_to_email(self):
        pass



class SendOTPFR(NotificationService):
    def send_to_phone(self):
        send =  '''   <Phone>+33 6 12 34 56 78</Phone>
                    <Text> Your temporary code is : 5555</Text>
                '''
        print(send)


    def send_to_email(self):
        print('OTP was send to your email')



class SendOTPUSA(NotificationService):
    def send_to_phone(self):
        send = {
            "phone": "+1 332 331 1843",
            "text": "Your temporary code is : 5555"
        }
        print(send)

    def send_to_email(self):
        print('OTP was send to your email')

otp_fr = SendOTPFR()
otp_usa = SendOTPUSA()