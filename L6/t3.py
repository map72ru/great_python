
class Worker:

    def __init__(self):
        self.name = None
        self.surname = None
        self.position = None
        self._income = {'wage': 45000, 'bonus': 720000}

class Position(Worker):

    def get_full_name(self):
        full_name = ''
        if self.name is not None:
            full_name += self.name + ' '

        if (self.surname is not None):
            full_name += self.surname

        return full_name.rstrip()

    def total_income(self):
        return self._income['wage'] + self._income['bonus']


wrk = Position()
wrk.name = 'Jim'
wrk.surname = 'Carrey'

print(wrk.get_full_name())
print(wrk.total_income())