#Components of sys will be used to allow players to exit game
import sys

#conatins the functionality needed to make the game
import pygame

from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def _init_(self):
        """Initialize the game, and create game resources."""
        #initializes the necessary background settings for game
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # set the background color.
        self.bg_color = (230,230,230)#(red,green,blue) values from 0-255. equal mix of red,green,and blue
        #creates light grey color

#How the game is controlled.
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            #An event is an action that the user performs while playing the game
            for event in pygame.event.get():#returns a list of events that have taken place since the last time this function was called.
                if event.type == pyame.QUIT:
                    sys.exit()
            
            #redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)#fills the background color

            # make the most recently drawn screen visible
            pygame.display.flip()
            #continually updates the display to show the new positions of game elements and hides the old ones,
            #creating the illusion of smooth movement
if _name_ == '_main_':
    #make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()