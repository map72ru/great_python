from time import sleep
from itertools import cycle

class TrafficLight:

    def __init__(self):
        self.__color = None
        self.__intervals = {'red':7, 'yellow': 2, 'green': 10}

    def running(self):
        iterator = cycle(self.__intervals.keys())

        n = 5
        while True:
            self.__color = next(iterator)
            print('Color: ', self.__color)
            sleep(self.__intervals[self.__color])
            n -= 1
            if n == 0:
                break


tf = TrafficLight()
tf.running()


