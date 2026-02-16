class Student:
    graduation = 11

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def describe(self):
        return f"{self.name} is the students name"
    
    def action(self):
        remain = self.graduation - self.grade
        return f"{remain} years until graduation"
    
student1 = Student("Lisa", 15, 8)
student2 = Student("Mike", 5, 3)

print(student1.action())
print(student1.age)
print(student2.describe())
print(student2.grade)

