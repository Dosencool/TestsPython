import pygame
import sys
import random

class snake(object):
    pass
    def get_head_postion(self):
        pass



   def turn(self, point):
    pass
    
        def move(self):
    pass

    
        def reset(self):
    pass
    
    def draw(self, surface):
    pass
    
    def handle(self):
    pass 



class food(object):
    def _init_(self):
        pass

    def randomize_position(self):
        pass

    def draw(self, surface):
        pass


def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 ==0:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (84, 194, 205), rr)





SCREEEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1,0)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SCREEEN_WIDTH, SCREEN_HEIGHT, O, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = snake()
    food = food()


    score = 0
    while (True):
        clock.tick(10)
        #handle events
        screen.blit(surface, (0, 0))
        pygame.dysplay.update()

main()