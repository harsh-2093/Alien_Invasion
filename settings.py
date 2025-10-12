class Settings:
    """A class to store all settings for Alien Invasion"""
    
    def __init__(self):
        """initialize the games's setting"""
        #screen setting
        self.screen_width=1200
        self.screen_height=600
        self.bg_color=((230,230,230))
        self.bullet_allowed=3
        self.ship_speed=4.5
        
        #bullet settings
        self.bullet_speed=2.0
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        