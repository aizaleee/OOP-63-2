class Hero:
    def __init__(self, nick, hp, lvl) :
       # pass
        self.nick = nick
        self.hero = hp
        self.lvl = lvl

       

        def action(self):
            return f" {self.nick} base action activate"
        
        #дочерний класс
class MageHero(Hero):

    def __init__(self, nick, hp, lvl, mp):
        super().__init__(nick, hp, lvl)
        self.mp = mp

        def action(self):
            return f" this is daughter class {self.nick} "
        
asuna = Hero("Asuna", 999, 99999)
mage_kirito = MageHero("Aiz", 100, 1000, 99)

print(mage_kirito.action())
print(asuna.action)


class Animal:
    def action(self):
        print (f"base")
    

class Fly(Animal):
    def action(self):
        print (f"fly")
    
class Swim(Animal):
    def action(self):
        print (f"swim")
    
class Duck(Fly, Swim):
    def action(self):
        print (f"Duck")

donald_duck = Duck()
donald_duck.action()
print(Duck.__mro__)
            
             


