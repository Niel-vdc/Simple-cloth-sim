from math import *
import pygame
from chord import *

class Spring(Chord):
    def __init__(self, A, B, strength=0.5, colour=(0, 0, 0), width=2) -> None:
        super().__init__(A, B, colour, width)
        self.rest = dist(A.pos, B.pos)
        self.strength = strength # between 0 and 1

    def draw(self, screen):
        pygame.draw.line(screen, self.colour, (self.A.pos), self.B.pos, self.width)
        self.stretch()
    
    def stretch(self):
        error = (dist(self.A.pos, self.B.pos) - self.rest)/self.rest

        self.B.apply_force(error*self.strength, error*self.strength)
