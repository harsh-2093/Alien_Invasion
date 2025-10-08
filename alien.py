import pygame

class Alien:
    """Class to manage the alien"""
    def __init__(self,ai_game):
        """initialize the alien ans set its start posn"""
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        
        #load the alien and get recr()
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()
        
        self.rect.midtop=self.screen_rect.midtop
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
        
    