import sys
import random
from Player import Player

TRIALS = 2

class Computer(Player):
    """ class representating a computer wich can play the VirusGame """

    def __init__(self, name, color):

        super().__init__(name, color)

    def play(self, grid):
        """ Compute the best move to play """

        self.random_play(grid)
        self.adversary.play(grid)

    def max_min_computation(self, grid):
        """ Comput the best move to play with min_max """

        pass

    def random_play(self, grid):
        """ Play at a random position """

        random_choice = random.choice(grid.empty_square())
        grid.add_a_pawn(self.color, random_choice[0], random_choice[1])


    def valuate_grid(self, grid):
        """ 
        Valuate the situation of a grid
        return the score of the situation
        +1 For possesing pawn
        -1 For not possessing pawn
        0 for None playing
        """
        size = len(grid)
        score = 0

        for x in range(size):
            for y in range(size):
                if grid[x][y] == None:
                    continue

                if grid[x][y].color == self.color:
                    score += 1
                else:
                    score -= 1

