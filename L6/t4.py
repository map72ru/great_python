class Car:

    def __init__(self):
        self.speed = None
        self.color = None
        self.name = None
        self.is_police = False

    def go(self):
        print('The car \'', self.name or 'Noname', '\' is go')

    def stop(self):
        print('The car \'', self.name or 'Noname', '\' stopped')


    def turn(self, direction: str):
        print('The car \'', self.name or 'Noname', '\' turned ', direction)


    def show_speed(self, speed):
        self.speed = speed
        print('Current speed:', speed)

class TownCar(Car):

    def show_speed(self, speed):
        if (speed > 60):
            print('Crazy speed: ', speed)
        else:
            super(TownCar, self).show_speed(speed)


class WorkCar(Car):

    def show_speed(self, speed):
        if (speed > 40):
            print('Crazy. crazy speed: ', speed)
        else:
            super(WorkCar, self).show_speed(speed)


class SportCar(Car):
    pass


class PoliceCar(Car):

    def __init__(self):
        super().__init__()
        self.is_police = True


workCar = WorkCar()
workCar.name = 'KAMAZ'
workCar.go()
workCar.turn('left')
workCar.turn('right')
workCar.show_speed(55)
workCar.stop()


townCar = TownCar()
townCar.name = 'AUTOBUS'
townCar.go()
townCar.turn('right')
townCar.turn('left')
townCar.show_speed(55)
townCar.stop()


sportCar = SportCar()
sportCar.name = 'Jaguar F-Type'
sportCar.go()
sportCar.turn('right')
sportCar.turn('left')
sportCar.show_speed(278)
sportCar.stop()
