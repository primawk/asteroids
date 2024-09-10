from circleshape import * 
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y = y
    
    def draw(self, screen):
        pygame.draw.circle(screen,'white', self.position, SHOT_RADIUS, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
  