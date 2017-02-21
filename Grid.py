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
        if x_position > len(self.grid) or y_position > len(self.grid):
            return False

        if not self.grid[x_position][y_position] is None:
            return False

        self.grid[x_position][y_position] = Pawn(color)
        size = len(self.grid)
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x + x_position >= 0 or x + x_position - 1 < size:
                    if y + y_position >= 0 or y + y_position - 1 < size:
                        try:
                            self.grid[x_position + x][y_position + y].change_color(color)
                        except:
                            pass

    def is_finished(self):
        """
        Return True if all the cell's grid have a pawn
        Return False if a None or more are in the grid
        """
        for line in self.grid:
            if None in line:
                return False
        return True

    def __repr__(self):
        repr_string = ""

        for x in range(len(self.grid)):
            for y in range(len(self.grid)):
                if self.grid[x][y] == None:
                    repr_string += "."
                else:
                    repr_string += str(self.grid[x][y])
                repr_string += "\t"

            repr_string += "\n"

        return repr_string

    def copy(self):
        """ Return a copy of the grid (including copying pawn) """

        size = len(self.grid)
        new_grid = Grid(size)

        for x in range(size):
            for y in range(size):
                if self.grid[x][y] != None:
                    new_grid.add_a_pawn(self.grid[x][y].color, x, y)

        return new_grid


    def empty_square(self):
        """ Return list of empty square in the grid """
        size = len(self.grid)
        return [(x, y) for y in range(size) for x in range(size) if self.grid[x][y] == None]

    def give_winner(self):
        """
        give_winner return a str announcement of the winner
        Browsing the grid, the methode define what pwan are more present
        return exemple:
        >>> red player is the winner
        """
        # Define what are the color of pwan by browsing self.grid and scoring
        players = {}
        for line in self.grid:
            for cell in line:
                if cell != None and cell not in players:
                    players[cell.color] = 1
                if cell != None and cell in players:
                    players[cell.color] += 1

        return (max(players, key=lambda k: players[k]), ' players are the winner')
