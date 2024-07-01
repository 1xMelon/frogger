import GameObject
import random
class Fly(GameObject):
    def __init__(self, x, y, width, height, color):
        super(). __init__(x, y, width, height, color)

    def teleport(self):
        timer = random.randint(10000, 25000)