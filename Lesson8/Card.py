from random import randint

class Card:

    def __init__(self):
        self.__numbers = [[None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None, None]]

    def generate(self):
        i = 0
        temp_list = []
        while True:
            '''позиция в строке'''
            c = randint(0, 8)
            '''Проверим, занята ли позиция'''
            while self.__numbers[i][c] is not None:
                c = randint(0, 8)
            '''номер бочонка'''
            n = randint(1, 90)
            '''Проверим, был ли такой бочонок'''
            while temp_list.count(n) > 0:
                n = randint(1, 90)

            self.__numbers[i][c] = n
            temp_list.append(n)
            if len(temp_list) == 15:
                break
            if len(temp_list) % 5 == 0:
                i += 1

        for row in self.__numbers:
             self.__sort(row)

    def check(self, n):
        if self.exist_number(n):
            if self.is_empty_numbers():
                return -1
            else:
                return 1

        return 0

    def __str__(self):
        return '\n'.join ([' '.join (['{0:2d}'.format(elem) if elem is not None else '  'for elem in line ]) for line in self.__numbers])

    def is_empty_numbers(self):
        return sum([sum([1 if n is not None else 0 for n in row]) for row in self.__numbers]) == 0

    def exist_number(self, elm):
        i = 0
        for row in self.__numbers:
            j = 0
            for n in row:
                if n == elm:
                    self.__numbers[i][j] = None
                    return True
                j += 1
            i += 1
        return False

    def __sort(self, row: list):
        elms = [n for n in row if n is not None]
        elms.sort()
        m = k = 0
        for n in row:
            if n is not None:
                row[m] = elms[k]
                k += 1
            m += 1