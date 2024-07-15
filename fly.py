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

    def check_on_fly(self, frog, goal1, goal2, goal3, goal4):
        on1 = False
        on2 = False
        on3 = False
        on4 = False
        if self.hitbox.colliderect(frog.hitbox):
            if self.hitbox.colliderect(goal1.hitbox):
                on1 = True
            if self.hitbox.colliderect(goal2.hitbox):
                on2 = True
            if self.hitbox.colliderect(goal3.hitbox):
                on3 = True
            if self.hitbox.colliderect(goal4.hitbox):
                on4 = True

        if on1 == True:
            self.goal_positions.remove[0]
        if on2 == True:
            self.goal_positions.remove[1]
        if on3 == True:
            self.goal_positions.remove[2]
        if on4 == True:
            self.goal_positions.remove[3]