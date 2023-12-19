import pygame
from pygame.locals import *


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):

        # Perform one-time initialization
        if self.on_init() == False:
            self._running = False

        while self._running:

            # Process events
            for event in pygame.event.get():
                self.on_event(event)

            # Process game logic
            self.on_loop()

            # Draw
            self.on_render()

        # Game loop has exited, clean up
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
