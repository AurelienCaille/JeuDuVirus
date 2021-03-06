""" Module comprising the Pawn class """
class Pawn(object):
    """ Class representating a pawn of the game """

    def __init__(self, color):
        """
        self.color Color of the pawn and player owner
        """

        self.color = color

    def change_color(self, color):
        """ Change the color of the pawn to the new color """
        self.color = color

    def __repr__(self):
        return str(self.color)

    def __str__(self):
        return str(self.color)
