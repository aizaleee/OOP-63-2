from shutil import move


class Person:
    def __init__(self):
        self._age = None

    def set_age(self, age):
        if age < 0:
            print("invalid age")
        else:
            self._age = age


    def get_age(self):
        return self._age
    
p = Person()
p.set_age(25)
print(p.get_age())  # Вывод: 25
p.set_age(-5)  # Должна быть ошибка или предупреждение

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return 'I am an animal'


class Dog(Animal):
    def speak(self):
        return 'Woof'

class Cat(Animal):
    def speak(self):
        return 'Meow'


dog = Dog("Buddy")
cat = Cat("Kitty")
print(dog.name, dog.speak())  # Вывод: Buddy Woof
print(cat.name, cat.speak())  # Вывод: Kitty Meow


class Vehicle:
    def move(self):
        return 'Vehicle is moving'
    
class Car(Vehicle):
    def move(self):
        return 'car is driving '
    
class Bicycle(Vehicle):
    def move(self):
        return f'Bicycle is pedaling'
    
def move(vehicle):
    return vehicle.move()
    

car = Car()
bike = Bicycle()

print(move(car))  # Вывод: Car is driving
print(move(bike))  # Вывод: Bicycle is pedaling
     
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height
    
    def area(self):
        return self.length * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * 3.14
    
    
    
    
rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())  # Вывод: 50
print(circle.area())  # Вывод: ~153.94


     
     
