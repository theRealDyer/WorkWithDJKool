# Hi Andrew :)

# Very basic setup for running a black screen at specified resolution.

import pygame, sys
from settings import *
from debug import *

class Game:
    def __init__(self):
        
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('The Game')
        self.clock = pygame.time.Clock()

        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            
            self.screen.fill('black')

            # run debugger
            debug(pygame.mouse.get_pos())
            debug(pygame.mouse.get_pressed(), 40)
            

            pygame.display.update()
            self.clock.tick(FPS)

            
  

if __name__ == '__main__':
    game = Game()
    game.run()





