import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape, pygame.sprite.Sprite):
    containers = ()

    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self, self.containers)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
