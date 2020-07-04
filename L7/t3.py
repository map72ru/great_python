class Cell:

    def __init__(self, psize: int):
        if psize <= 0:
            raise ValueError('Cell size can''t less than 0')
        self.__size = psize

    @property
    def size(self):
        return self.__size

    def __add__(self, other):
        return Cell(self.size + other.size)

    def __sub__(self, other):
        if self.size <= other.size:
            raise ValueError(f'Invalid cells {other.size} >= {self.size}')
        return Cell(self.size - other.size)

    def __mul__(self, other):
        return Cell(self.__size * other.size)

    def __truediv__(self, other):
        return Cell(int(self.__size / other.size))

    def __str__(self):
        return f'Cell: {self.__size}'

    def make_order(self, n: int):
        s = ''
        s += ('*' * n + '\n') * int(self.__size / n)
        s += ('*' * (self.__size - n * int(self.__size / n) ) + '\n')
        return s


c1 = Cell(7)
c2 = Cell(5)

print('c1+c2:')
print(c1 + c2)
print((c1 + c2).make_order(5))

print('c1-c2:')
print(c1 - c2)
print((c1 - c2).make_order(5))

print('c1*c2:')
print(c1 * c2)
print((c1 * c2).make_order(5))

print('c1/c2:')
print(c1 / c2)
print((c1 / c2).make_order(5))