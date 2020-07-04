from abc import ABC, abstractmethod

class Dress(ABC):

    def __init__(self, size: float, height: float):
        self.__size = size
        self.__height = height

    @abstractmethod
    def materials_size(self):
        pass

    @property
    def size(self):
        return self.__size

    @property
    def height(self):
        return self.__height

class Coat(Dress):

    def materials_size(self):
        return self.size/6.5 + 0.5

class Suit(Dress):

    def materials_size(self):
        return 2*self.height + 0.3


coat = Coat(52, 180)
print(f'Coat materials size: {coat.materials_size()} on size: {coat.size} and height: {coat.height}')

suit = Suit(52, 180)
print(f'Suit materials size: {suit.materials_size()} on size: {suit.size} and height: {suit.height}')