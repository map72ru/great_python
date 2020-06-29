
class Road:

    __ASPHALT_DENSITY = 25

    def __init__(self, length: float, width: float):
        self._length = length
        self._width = width

    def calculate_mass(self, depth: float):
        print(f'Mass: {self._width * self._length * self.__ASPHALT_DENSITY * depth/1000}')


road = Road(5000, 20)

road.calculate_mass(5)