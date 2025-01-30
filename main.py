import sys
import pygame                                                               # import pygame
from constants import *                                                     # import from constants.py file
from player import *                                                        # import from player.py file
from asteroid import *                                                      # import from asteroid.py
from asteroidfield import *                                                 # import from asteroidfield.py
from shot import *

def main():
    pygame.init()                                                           #initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))         # screen resolution imported from constants
    clock = pygame.time.Clock()                                             # Clock object
    
    updatable = pygame.sprite.Group()                                       # updatable group
    drawable = pygame.sprite.Group()                                        # drawable group
    asteroids = pygame.sprite.Group()                                       # asteroids group
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)  
   
    Asteroid.containers = (asteroids, updatable, drawable)                  # container for asteroid groups
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)                               # container for player groups (venn diagram)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)                        # player object drawn from Player instance Class
    dt = 0                                                                  # delta time
    
    while True:                                                             # inf while loop
        for event in pygame.event.get():                                    
            if event.type == pygame.QUIT:                                   # when x'ing game python code stops
                return
        
        updatable.update(dt)                                                # player rotation and movement (wasd)
        
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

            for bullet in shots:
                if asteroid.collision(bullet):
                    asteroid.split()
                    bullet.kill()
        
        screen.fill((0,0,0))                                                # black color 
        
        for obj in drawable:                                                # for loop for object in drawable
            obj.draw(screen)                                                # player character on screen
        
        pygame.display.flip()                                               # idk
        
        dt = clock.tick(60)/1000                                            # frame limit
        



if __name__ == "__main__":
    main()