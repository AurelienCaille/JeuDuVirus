class Pion(object):
    """ Class representating a pion of the game """

    def __init__(self, color):

        self.color = color

    def change_color(self, color):
        """ Change the color of the pion to the new color """
        self.color = color
