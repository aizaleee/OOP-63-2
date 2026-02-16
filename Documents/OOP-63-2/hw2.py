class Worker:
    def __init__(self, name):
        self.name = name

    def work(self):
        return f"{self.name} Worker is working "
    

class Developer(Worker):

    def work(self):
        return f'{self.name } is a developer writes code'


class Designer(Worker):
    
    def work(self):
        return f"{self.name } is designer designs obv"
    
workers = [
    Developer("Alex"),
    Designer("Kate"),
    Worker("Sam")
]

for worker in workers:
   print( worker.work())

