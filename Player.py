class Player(object):
    def __init__(self, name, color):

        self.name = name
        self.color = color
        self.point = 0
        self.adversary = None

    def get_adversary(self):
        return self.adversary
    
    def set_adversary(self, adversary):
        self.adversary = adversary