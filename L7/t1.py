class Matrix:

    def __init__(self, data: list = None):
        self.__elements = []

        i = 0
        if (data is not None):
            for row in data:
                j = 0
                r = []
                for col in row:
                     r.append(col)
                     j += 1
                self.__elements.append(r)
                i += 1
        self.__size = i

    @property
    def size(self):
        return self.__size

    def __str__(self):
        s = ''
        for row in self.__elements:
            for col in row:
                 s += str(col) + ' '
            s = s.rstrip() + '\n'
        return s

    def __iter__(self):
        self.__next_index = 0
        return self

    def __next__(self):
        if self.__next_index < self.size:
            next = self.__elements[self.__next_index]
            self.__next_index += 1
            return next
        raise StopIteration

    def __getitem__(self, item):
        if item < 0 and item >= self.size:
            raise IndexError(f'Индекс вне диапазона {item}')

        return self.__elements[item]

    def append(self, row):
        self.__elements.append(row)

    def __add__(self, other):

        if type(other) is not Matrix:
            raise ValueError('Объект не класса Matrix')

        if self.size != other.size:
            raise ValueError('Размер матрицы не совпадают')


        outMatrix = Matrix()

        i = 0
        for row in other:
            j = 0
            r = []
            if len(other[i]) != len(self.__elements[i]):
                raise ValueError(f'Размер {i} строки не совпадают')

            for col in row:
                 r.append(self.__elements[i][j] + col)
                 j += 1
            outMatrix.append(r)
            i += 1

        return outMatrix


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print('M1:')
print(m1)

print('M2:')
print(m2)

print('M1 + M2:')
print(m1 + m2)