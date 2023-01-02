import random

class dice():
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randrange(1,int(self.sides)+1)
