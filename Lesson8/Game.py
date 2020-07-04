from random import randint
from Lesson8.Exceptions import GameStopException, IamWinException

class Game:

    def __init__(self, player1, player2):
        self.__player1 = player1
        self.__player2 = player2

    def show(self):
        print(f'---------- {self.__player1.name} -------------')
        print(self.__player1.card)
        print('\n')
        print(f'---------- {self.__player2.name} --------------')
        print(self.__player2.card)

    def play(self):

        __numbers = []
        while True:
            n = randint(1, 90)
            while __numbers.count(n) > 0:
                n = randint(1, 90)

            print(f'Следующий бочонок: {n}')
            __numbers.append(n)
            if len(__numbers) == 90:
                break

            try:
                self.__player1.check(n)
                self.__player2.check(n)
            except IamWinException as x:
                print(f'\nИгра завершена. Выиграл игрок: {x.player.name}')
                break
            except GameStopException as x:
                print(f'\nИгра завершена. Проиграл игрок: {x.player.name}')
                break

            self.show()

    def start(self):
        '''
Правила игры:
    Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
    и фишек (бочонков) с цифрами.

    Количество бочонков — 90 штук (с цифрами от 1 до 90).

    Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
    Если игрок выбрал "зачеркнуть":
        Если цифра есть на карточке - она зачеркивается и игра продолжается.
        Если цифры на карточке нет - игрок проигрывает и игра завершается.

    Если игрок выбрал "продолжить":
        Если цифра есть на карточке - игрок проигрывает и игра завершается.
        Если цифры на карточке нет - игра продолжается.

    Побеждает тот, кто первый закроет все числа на своей карточке.
        '''
        print(self.start.__doc__)

        self.__player1.init()
        self.__player2.init()

        self.show()

        self.play()