import pygame                                                               # import pygame
from constants import *                                                     # import from other py file
from player import *                                         

def main():
    pygame.init()                                                           #initialize pygame
    clock = pygame.time.Clock()                                             # Clock object
    dt = 0                                                                  # delta time
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))         # screen resolution imported from constants
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:                                                             # inf while loop
        for event in pygame.event.get():                                    
            if event.type == pygame.QUIT:                                   # when x'ing game python code stops
                return
        
        screen.fill((0,0,0))                                                # black color
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()                                               # idk
        dt = clock.tick(60)/1000                                            # frame limit
        



if __name__ == "__main__":
    main()