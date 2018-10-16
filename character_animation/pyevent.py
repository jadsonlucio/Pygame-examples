import pygame

class Events:
    def __init__(self):
        self.after_events = []
        self.callback_events = []

        self.dict_events = {
            pygame.KEYUP : self.key_release,
            pygame.KEYDOWN : self.key_press,
            pygame.MOUSEMOTION : self.mouse_move
        }

    def mouse_move(self, event):
        pass

    def key_press(self, event):
        pass

    def key_release(self, event):
        pass

    def add_after_event(self, time, callback):
        self.after_events.append((time, callback))