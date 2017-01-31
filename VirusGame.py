""" Module comprising the VirusGame class """
from Grid import Grid

class VirusGame(object):
    """ Class representating a VirusGame and control it """

    def __init__(self, size, first_player):
        """
        :self.grid Grid of the game
        :self.first_player Player who play in first in the game
        """

        self.grid = Grid(size)
        self.first_player = first_player

    def play(self):
        """ Launch the game """
        self.first_player.play(self.grid)

