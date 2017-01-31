from Grid import Grid

class VirusGame(object):

    def __init__(self, size, first_player):
        """
        :self.grid Grid of the game
        :self.first_player Player who play in first in the game
        """

        self.grid = Grid(size)
        self.first_player = first_player

    def play(self):
        pass

