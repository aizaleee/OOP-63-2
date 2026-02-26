class User:
    def __init__(self, first_name, last_name, balance, bonus) :
        self.first_name = first_name
        self.last_name = last_name
        self._balance = balance
        self.bonus = bonus

    def get_balance(self):
        return self._balance
    
    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name
    
    @property
    def total_balance(self):
        return self._balance + self.bonus    
    
    @property
    def user_balance(self):
        return self._balance   
    
    @user_balance.setter
    def user_balance(self, value):
        if value < 0:
            print('Error')
        self._balance = value


ardager = User('Ardager', 'Pam ', 100, 50)

# print(ardager.first_name)
# print(ardager.get_balance())
# print(ardager.full_name)
# print(ardager.total_balance)



#decorator methods
# def simple_decorator(func):
#     def wrapper():
#         print('berofe')
#         func()
#         print('after')
#     return wrapper

# @simple_decorator
# def say_hello():
#     print('hello world')

# say_hello()

# def how(func):
#     def wrapper(imya):
#         func(imya)
#         print(f'so how is it goin {imya}')
#     return wrapper

# @how
# def greeting(name):
#     print(f'{name} hallooooo')

# greeting('ardager')


def repeat_decorator(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator

@repeat_decorator(5)
def say_hello():
    print('hello world')

say_hello()


def class_decorator(cls):
    class NewClass(cls):

        def method(self):
            print('new method')

    return NewClass

@class_decorator
class OldClass:
    def method(self):
        print("old method" )

obj1 = OldClass()

obj1.method()
