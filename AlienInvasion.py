#Components of sys will be used to allow players to exit game
import sys

#conatins the functionality needed to make the game 
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        #initializes the necessary background settings for game
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # set the background color.
        self.bg_color = (230,230,230)#(red,green,blue) values from 0-255. equal mix of red,green,and blue
        #creates light grey color

#How the game is controlled.
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    #Created a helper method for the check events to isolate the event management loop.
    # This allows you to manage events separately from other aspects of the game.         
    def _check_events(self):
        """Respond to the keypresses and mouse events."""
        for event in pygame.event.get():#returns a list of events that have taken place since the last time this function was called.
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN: # check to see if key has been pressed
                   self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT: 
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False # when player releases the right key, sets flag to false
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    # also created a helper method for the background section as well.
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)#fills the background color
        self.ship.blitme()

            # make the most recently drawn screen visible
            pygame.display.flip()
            #continually updates the display to show the new positions of game elements and hides the old ones,
            #creating the illusion of smooth movement
if __name__ == '__main__' :
    #make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()