import pygame
import sys
from constants import *
from player import *
from asteroidfield import *
from asteroid import *
from shot import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots)

    player = Player(x, y)
    asteroid_field = AsteroidField() 

    

    while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            return
        pygame.Surface.fill(screen, ('black'))
    

        for obj in updatable:
          obj.update(dt) 
    
        for obj in drawable:
          obj.draw(screen)

        for obj in shots:
          obj.draw(screen)
          obj.update(dt)

        for obj in asteroids:
          for bullet in shots:
            if obj.is_colliding(bullet) == True:
              obj.split()
              bullet.kill()

          if obj.is_colliding(player) == True:
            sys.exit("Game over!")

        pygame.display.flip()
      
        dt = clock.tick(60) / 1000  
        
if __name__ == "__main__":
    main()