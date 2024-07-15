from game_object import GameObject
import random
class Fly(GameObject):
    def __init__(self, x, y, width, height, color):
        super(). __init__(x, y, width, height, color)
        self.locked = False
        

    def teleport(self, goal_positions):
        self.position = random.choice(goal_positions)
        self.x = self.position[0]
        self.y = self.position[1]
