import random
from Player import Player

TRIALS = 4  # 4 become long


class Computer(Player):
    """ class representating a computer wich can play the VirusGame """

    def __init__(self, name, color):

        super().__init__(name, color)

    def play(self, grid):
        """ Compute the best move to play """

        # self.random_play(grid)
        print("Computing...")
        best_move = self.min_max_computation(grid, TRIALS)
        print("I play:", best_move)
        grid.add_a_pawn(self.color, best_move[0], best_move[1])
        print("______________________________")
        if grid.is_finished():
            print(grid.give_winner())

        else:
            self.adversary.play(grid)

    def min_max_computation(self, grid, trials):
        """
        Compute the best move with min max algorithm, return the "best" move
        """
        # Associate plays and score
        best_score = -float('inf')
        move = ()
        for empty in grid.empty_square():

            new_grid = grid.copy()
            new_grid.add_a_pawn(self.color, empty[0], empty[1])

            score = self.min_computation(grid, trials-1)

            if score > best_score:
                best_score = score
                move = empty

        return move

    def max_computation(self, grid, trials):
        """ Compute the max move for the adversary in min_max algorithm """

        if trials == 0 or grid.is_finished():
            return self.valuate_grid_score(grid)

        else:
            # Play
            plays = []
            for empty in grid.empty_square():
                new_grid = grid.copy()
                new_grid.add_a_pawn(self.color, empty[0], empty[1])
                plays.append(new_grid)

            # Return max of the player (create the recursivity)
            return max([self.min_computation(play, trials - 1) \
                        for play in plays])

    def min_computation(self, grid, trials):
        """ Compute the min move for the adversary in min_max algorithm """

        if trials == 0 or grid.is_finished():
            return self.valuate_grid_score(grid)

        else:
            # Play for the adversary
            plays = []
            for empty in grid.empty_square():
                new_grid = grid.copy()
                new_grid.add_a_pawn(self.adversary.color, empty[0], empty[1])
                plays.append(new_grid)

            # Return max of the player (create the recursivity)
            return min([self.max_computation(play, trials - 1) \
                        for play in plays])

    def random_play(self, grid):
        """ Play at a random position """

        random_choice = random.choice(grid.empty_square())
        grid.add_a_pawn(self.color, random_choice[0], random_choice[1])

    def valuate_grid_score(self, grid):
        """
        Valuate the situation of a grid
        return the score of the situation
        +1 For possesing pawn
        -1 For not possessing pawn
        0 for None playing
        """
        size = len(grid.grid)
        score = 0

        for x in range(size):
            for y in range(size):
                if grid.grid[x][y] is None:
                    continue
                else:
                    if grid.grid[x][y].color == self.color:
                        score += 1
                    else:
                        score -= 1
        return score

