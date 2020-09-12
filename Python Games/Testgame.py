import pygame

width, height = 2550,  1325
backgroundColor = 15, 0, 92

pygame.init()
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Test Game')

clock = pygame.time.Clock()

image = pygame.image.load("/Users/eliot/Development/TestsPython/Python Games/Dosencool.PNG")
rect = image.get_rect()

quitter = False
while not quitter:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Bye!")
            quitter = True


    surface.fill(backgroundColor)
    pygame.display.flip()
     surface.blit(image, rect)

    pygame.display.update()
    clock.tick(60)

    
#image = pygame.image.load("/Users/eliot/Development/TestsPython/Python Games/Dosencool.PNG")
#rect = image.get_rect()
#while True:
#	surface.fill(backgroundColor)
#	pygame.display.flip()
#	surface.blit(image, rect)