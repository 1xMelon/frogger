from game_object import GameObject
import random
class Fly(GameObject):
    def __init__(self, x, y, width, height, color):
        super(). __init__(x, y, width, height, color)
        self.goal_positions = [(55,50), (355,50), (555,50), (905,50)]

    def teleport(self):
        self.position = random.choice(self.goal_positions)
        self.x = self.position[0]
        self.y = self.position[1]