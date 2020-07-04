class GameStopException(Exception):

    def __init__(self, player):
        super().__init__()
        self.player = player

class IamWinException(GameStopException):

    def __init__(self, player):
        super().__init__(player)
