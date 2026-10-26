import pygame

from shared.constants import FPS, HEIGHT, WIDTH
from game.player import Player

width = 40
height = 60

pygame.init()

pygame.display.set_caption('TitanDash')
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

player = Player(100, 100, width, height)
platform = pygame.Rect(0, HEIGHT - 30, WIDTH, 30)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.QUIT:
            running = False

    player.loop(FPS)

    screen.fill((25, 25, 25))
    pygame.draw.rect(screen, (255, 255, 255), platform)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()