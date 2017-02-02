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

    def __repr__(self):
        repr_string = ""

        for x in range(len(self.grid)):
            for y in range(len(self.grid)):
                repr_string += str(self.grid[x][y])
                repr_string += "\t"
            
            repr_string += "\n"

        return repr_string

    def give_winner(self):
        """
        give_winner return a str announcement of the winner
        Browsing the grid, the methode define what pwan are more present
        return exemple:
        >>> red player is the winner
        """
        # Define what are the color of pwan by browsing self.grid
        score_player_0 = 0
        score_player_1 = 0
        players = []
        while len(players) != 2:
            for line in self.grid:
                for cell in line:
                    if self.grid[line]cell[] != None and if len(players) == 0:
                            players.append(self.grid[line]cell[].color)
                    if self.grid[line]cell[] != (players[0] and None) and len(players) == 1:
                         players.append(self.grid[line]cell[].color)
        
        # Counting numburs of pawns and scoring
        for line in self.grid:
                for cell in line:
                    if self.grid[line]cell[] == players[0]:
                        score_player_0 += 1
                    if self.grid[line]cell[] == players[1]:
                         score_player_1 +=1
        
        # Return in function of the score 
        if score_player_0 > score_player_1 :
            return (players[0].color, ' player is the winner')
        if score_player_1 > score_player_0 :
            return (players[1].color, ' player is the winner')
        if score_player_0 = score_player_1 :
            return (players[0].color, ' and ', players[1].color, ' are ex aequo')
        