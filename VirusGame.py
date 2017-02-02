""" Module comprising the VirusGame class """
from Grid import Grid
from Player import Player

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

if __name__ == "__main__":

    J_1 = Player("J1", "blue")
    J_2 = Player("J2", "red")

    J_1.set_adversary(J_2)
    J_2.set_adversary(J_1)

    VIRUSGAME = VirusGame(4, J_1)
    VIRUSGAME.play()

