class Hero:

    #конструктор класса
    def __init__(self, nick, hp, lvl):
        #атрибуты класса
        self.nick = nick
        self.hp = hp
        self.lvl = lvl


#method
    def action(self):
        return f"{self.nick} base action level"

#object/ обюект или экземпляр класса
kirito = Hero("Kirito", 1000, 100)
asuna = Hero("Asuna", 1100, 101)

print(kirito.hp)
print(kirito.action())
print(asuna.action())
