import pygame

screen_height = 800
width = 40
height = 60

class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)

    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(self.COLOR)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

        self.scale = screen_height / 900
        self.gravity = 0.6 * self.scale
        self.terminal_velocity = 20 * self.scale
        self.run_speed = 4 * self.scale

        self.on_ground = False
        self.facing_right = True

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel

    def move_right(self, vel):
        self.x_vel = vel

    def loop(self, fps):
        self.move(self.x_vel, self.y_vel)
        if not self.on_ground:
            self.velocity.y += self.gravity

            self.velocity.y = min(self.velocity.y, self.terminal_velocity)

        self.position += self.velocity

        self.rect.topleft = (self.position.x, self.position.y)