from Pawn import *

class Grid(object):
    """
    Class representing the grid of VirusGame
    """
    def __init__(self, lenght):
        """
        :attribut:
        :self.grid: 2 dimensions board representing the grid
        """
        self.grid = [[None for dummy_l in range(lenght)] for dummy_l in range(lenght)]

    def add_a_pawn(self, color, x_position, y_position):
        """
        Methode to add a player's pawn to the Grid
        """
        self.grid[y_position][x_position] = Pawn(color)

    def is_finished(self):
        """
        Return True if all the cell's grid have a pawn
        Return False if a None or more are in the grid
        """
        for line in self.grid:
            if None in line:
                return False
        return True
