import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class to manage the single alien of a fleet"""
    def __init__(self,ai_game):
        """initalize the alien and set its starting positiomn."""
        super().__init__()
        self.screen=ai_game.screen
        
        #load the alien image and set its rect attribute.
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()
        
        #start each new alien near the top left of the screen.
        
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        
        # store the alien exact horixontal posn.
        self.x=float(self.rect.x)
    
        
    