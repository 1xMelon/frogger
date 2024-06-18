import pygame
from frog import Frog
from obstacle import Obstacle
from game_object import GameObject
from log import Log
class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1000,1000))
        self.frog = Frog(100,950,50,50,50, (50, 168, 82))
        self.obstacle1 = Obstacle(496,600,100,50,7, "left", (227, 86, 86))
        self.obstacle2 = Obstacle(134,700,100,50,4, "right", (80, 222, 108))
        self.obstacle3 = Obstacle(345,800,100,50,8, "left", (235, 124, 68))
        self.log = Log(100, 150, 150, 100, (100,3,15), 3, "right")
        self.log2 = Log(400, 250, 150, 100, (100,3,15), 3, "right")
        self.log3 = Log(700, 350, 150, 100, (100,3,15), 3, "right")
        self.starting_zone = GameObject(0, 900, 1000, 100, (125, 117, 114))
        self.safe_zone = GameObject(0, 450, 1000, 100, (125, 117, 114))
        self.water = Obstacle(0,0, 1000, 450, 0, "left", (69, 141, 196))
        self.goal1 = GameObject(0,0,150,150, (255, 255, 0))
        self.goal2 = GameObject(300,0,150,150, (255, 255, 0))
        self.goal3 = GameObject(500,0,150,150, (255, 255, 0))
        self.goal4 = GameObject(1000-150,0,150,150, (255, 255, 0))
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.game_loop()




    def event_handler(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.frog.x += self.frog.speed
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.frog.x -= self.frog.speed
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.frog.y -= self.frog.speed
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.frog.y += self.frog.speed
    

    def game_loop(self):
        while True:
            self.clock.tick(self.fps)
            self.event_handler()
            self.frog.update()
            self.check_game_over()
            self.obstacle1.move()
            self.obstacle2.move()
            self.obstacle3.move()
            self.log.move()
            self.log2.move()
            self.log3.move()
            self.obstacle1.update()
            self.obstacle2.update()
            self.obstacle3.update()
            self.log.update()
            self.log2.update()
            self.log3.update()

            self.draw()
            pygame.display.update()

    def draw(self):
        self.window.fill((0,0,0))
        self.starting_zone.draw(self.window)
        self.water.draw(self.window)
        self.goal1.draw(self.window)
        self.goal2.draw(self.window)
        self.goal3.draw(self.window)
        self.goal4.draw(self.window)
        self.safe_zone.draw(self.window)
        self.obstacle1.draw(self.window)
        self.obstacle2.draw(self.window)
        self.obstacle3.draw(self.window)
        self.log.draw(self.window)
        self.log2.draw(self.window)
        self.log3.draw(self.window)
        self.frog.draw(self.window)
        pygame.display.update()

    def check_game_over(self):
        game_over = False
        win = False
        if self.obstacle1.hitbox.colliderect(self.frog.hitbox):
            game_over = True
        if self.obstacle2.hitbox.colliderect(self.frog.hitbox):
            game_over = True
        if self.obstacle3.hitbox.colliderect(self.frog.hitbox):
            game_over = True
        if self.water.hitbox.colliderect(self.frog.hitbox):
            game_over = True
        if self.log.hitbox.colliderect(self.frog.hitbox):
            game_over = False
        if self.log2.hitbox.colliderect(self.frog.hitbox):
            game_over = False
        if self.log3.hitbox.colliderect(self.frog.hitbox):
            game_over = False
        if self.goal1.hitbox.colliderect(self.frog.hitbox):
            win = True
        if self.goal2.hitbox.colliderect(self.frog.hitbox):
            win = True
        if self.goal3.hitbox.colliderect(self.frog.hitbox):
            win = True
        if self.goal4.hitbox.colliderect(self.frog.hitbox):
            win = True

        if game_over == True:
            pygame.quit()
            quit()
        if win == True:
            pass