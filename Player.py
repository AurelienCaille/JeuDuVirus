""" Module comprising the Player class """
class Player(object):
    """ class representating a player """
    def __init__(self, name, color):
        """
        :self.name name of the Player
        :self.color color of the Player
        :self.point point of the Player, start with 0
        :self.adversary player adversary of the player, need to set it after each initialisation
        """

        self.name = name
        self.color = color
        self.point = 0
        self.adversary = None

    def get_adversary(self):
        """ Return adversary of the player """
        return self.adversary

    def set_adversary(self, adversary):
        """ Set the adversary of the player """
        self.adversary = adversary
