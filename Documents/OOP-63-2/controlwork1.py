class Hero:
    def __init__(self, name, lvl, hp) :
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f" {self.name} готов к бою"
    
    def __str__(self) -> str:
        return self.name
    
class MageHero(Hero):

    def __init__(self, name, hp, lvl, mp):
        super().__init__(name, hp, lvl)
        self.mp = mp

    def action(self):
        return f" Mar {self.name} кастует заклинание! MP: {self.mp}" 
    

    
class WarriorHero(MageHero):
    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"
    

mage1 = MageHero("Merlin", 80, 500, 150)
mage2 = MageHero("Merlin", 80, 500, 200)
warrior = WarriorHero("Conan", 50, 900, 20)



class BankAccount:
    def __init__(self, name, balance, password, bank_name):
        self.name = name
        self._balance = balance
        self.__password = password
        self.bank_name = bank_name


    def login(self, login, password):
        if self.login == login and self.__password == password:
            return print("OK!!")
        else:
            return print("Неверный логин или пароль!!")
        
    
    def full_info(self, hero,  balance):
        self.hero = hero
        self._balance = balance
        return f"  Ваша информация: {self.hero} n\\ Ваш баланс: {self._balance} "   
    
    def get_bank_name(self):
        return self.bank_name
    
    def bonus_for_level(self):
        return self.name.lvl * 10
    
    def __str__(self,  ):
        return f"{self.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.name) == type(other.name):
             return self._balance + other._balance
        else:
            return "Ошибка: разные типы героев"

    def __eq__(self, other):
        return (
        self.name.name == other.name.name and
        self.name.lvl == other.name.lvl
    )
        

acc1 = BankAccount(mage1, 5000, "1234", "Simba")
acc2 = BankAccount(mage2, 3000, "0000", "Simba")
acc3 = BankAccount(warrior, 2500, "1111", "Simba")



from abc import ABC, abstractmethod
class SendOTP(ABC):
    @abstractmethod
    def send_otp(phone):
        pass

class KGSms(SendOTP):

    def send_otp_to_phone(self):
        send = ''''
        <text>Код: 1234</text><phone>{phone}</phone>

        '''
        print(send)

class RUSms(SendOTP):
    def send_otp_to_phone(self):
        send = {
            {"text": "Код: 1234", "phone": "{phone}"}

        }
        print(send)


print(mage1.action())
print(warrior.action())
print(acc1)
print(acc2)
print("Банк:", acc1.get_bank_name())
print("Бонус зауровень:", acc1.bonus_for_level(), "SOM")

# --- Магические методы: __add__ ---
print("\n=== Проверка __add__ ===")
print("Сумма счетов двух магов:", acc1 + acc2)


# --- Магический метод: __eq__ ---
print("\n=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)  # True — одинаковое имя и уровень
print("Mage1 == Warrior ?", acc1 == acc3)  # False

# --- SMS ---
sms = KGSms()
print("\n", sms.send_otp("+996777123456"))
