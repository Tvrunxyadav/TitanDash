import pygame

pygame.init()

pygame.display.set_caption('TitanDash')
screen = pygame.display.set_mode((1200, 800))

clock = pygame.time.Clock()

while True:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)