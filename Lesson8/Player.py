from Lesson8.Card import Card
from Lesson8.Exceptions import IamWinException, GameStopException

class Player:

    def __init__(self, name):
        self.name = name
        self.__auto = False
        self.__card = Card()

    def init(self):
        self.__card.generate()

    def check(self, n):
        check = self.__card.check(n)
        result = input('Зачеркнуть цифру (y/n:д/н)? ')
        if result.lower() == 'д' or result.lower() == 'y':
            if check == -1:
                raise IamWinException(self)
            elif check == 0:
                raise GameStopException(self)
        else:
            if check == 1:
                raise GameStopException(self)



    @property
    def card(self):
        return self.__card

class Computer(Player):

    def __init__(self):
        super().__init__('Компьютер')
        self.__auto = True

    def check(self, n):
        if self.card.check(n) == -1:
            raise IamWinException(self)

