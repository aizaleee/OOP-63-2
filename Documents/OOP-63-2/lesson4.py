#магические методы or double unedrline

# class Test:
#     def __init__(self, value):
#         self.value = value

#     def __str__(self) -> str:   #str here same as print 
#         return str(self.value)


# test_obj = Test('just value')
# my_int = int(123)

# print(my_int)
# print(test_obj)


# class MyList:

#     def __init__(self, value):
#         self.value = value

#     def __add__ (self, other):
#         return self.value + other.value
    
#     def __str__(self) -> str:
#         return str(self.value)
    
#     def __init__ (self, array):
#         self.array = array
    
#     def __getitem__ (self, item):
#         return self.array[item]
    
# my_list = MyList([234, 234, 12, 23])

# # print(my_list[3])

# class MyInt:
# # my_int1 = MyInt(12)
# my_int2 = MyInt(10)
# my_int3 = my_int1 + my_int2
# print(my_int2)
# print(my_int1)
# print(my_int3)


class BankAccount:
    def __init__(self, name, balance):
        self.name = "hello"
        self.balance = balance

        print(self.name)


    def just_method(self):
        return self.name
    

    def static_method():


    def static_method(cls):
        
#class method for атрибуты