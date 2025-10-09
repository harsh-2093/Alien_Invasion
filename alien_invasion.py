import sys

import pygame

from settings import Settings

from ship import Ship
from alien import Alien


class AlienInvasion:
    '''overall class to manage game assets and behaviour.'''
    
    def __init__(self):
        """initialize the game, and create game resources"""
        
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship=Ship(self)
        self.alien=Alien(self)
        
    def run_game(self):
        """start the main loop for the game"""
        while True:
            #watch for keyboard and mouse event
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
    def _check_events(self):
        """respond to keypress and mouse event"""
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    #move the ship to the right
                    self.ship.moving_right=True
                elif event.type==pygame.K_LEFT:
                    #move the ship to the left
                    self.ship.moving_left=True
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    self.ship.moving_right=False
                elif event.type==pygame.K_LEFT:
                    self.ship.moving_left=False
    def _update_screen(self):
        """update images on the screen, and flip the new screen"""            
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.alien.blitme()
        
        pygame.display.flip()
if __name__=='__main__':
    #make a game instance , and run the game.
    ai=AlienInvasion()
    ai.run_game()