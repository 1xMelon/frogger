from game_object import GameObject
class Log(GameObject):
    def __init__(self, x, y, width, height, color, speed):
        super(). __init__(x, y, width, height, color)
        self.speed = speed