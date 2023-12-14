# Useful debug function that lets you pop a text box up 
# anywhere and analyse mouse_pos, key_press, etc

# Update: To be implemented at a later date as per Andrew's suggestion:
'''
pygame.init() should only be called once (in the "Game" initialization), but this 
would mean you'd have to delay the creation of the debug font until that happens. 
This is where the controlled initialization of all game "systems", even those in 
other modules, is important.
We can model a debug system the same way we model our other systems and use it to
provide all the additional overlay data we might need during development. That 
way we can just "disable" (not enable) the system in production environments. We 
can design this more later.
'''

import pygame
pygame.init()
font = pygame.font.Font(None, 30)

def debug(info, y = 10, x = 10):
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft = (x, y))
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)