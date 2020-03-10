import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen #assign the screen to an attribute of Ship, so we can access it easily in all methods in this class
        self.screen_rect = ai_game.screen.get_rect() #acess the screen's rect attribute. allows us to place the ship in the correct location on the screen  
        
        # load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start with each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        