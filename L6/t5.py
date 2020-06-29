class Stationery:

    _title = ''

    def draw(self):
        raise Exception('Abstract method')

class Pen(Stationery):

    def __init__(self):
        self._title = 'pen'

    def draw(self):
        print(f'The letter wrote by {self._title}')


class Pencil(Stationery):

    def __init__(self):
        self._title = 'pencil'

    def draw(self):
        print(f'{self._title} draw a circle')

class Handle(Stationery):

    def __init__(self):
        self._title = 'handle'

    def draw(self):
        print(f'{self._title} draw a line')



pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
