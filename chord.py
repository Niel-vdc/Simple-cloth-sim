from math import *
import pygame
import pygame.mouse
from particle import *

class Chord:
    def __init__(self, A, B, colour=(0, 0, 0), width=2, elasticity=0.6) -> None:
        self.A = A
        self.B = B
        self.rest = dist(A.pos, B.pos)
        self.colour = colour
        self.width = width
        self.elasticity = elasticity

    def draw(self, screen):
        pygame.draw.line(screen, self.colour, (self.A.pos), self.B.pos, self.width)
        self.cut()

    def pull(self, pxpm):
        force = pygame.Vector2((self.B.pos.x - self.A.pos.x)/pxpm * self.elasticity, (self.B.pos.y - self.A.pos.y)/pxpm * self.elasticity) 
        if dist(self.A.pos, self.B.pos) > self.rest:
            self.A.apply_force(force)
            self.B.apply_force(-force) #Newton III
    

        # if dist(self.A.pos, self.B.pos) < self.rest:
        #     self.A.apply_force(-force)
        #     self.B.apply_force(force) #Newton III

    def getGradient(self):
        if (self.A.pos.x - self.B.pos.x) != 0:
            return (self.A.pos.y - self.B.pos.y) / (self.A.pos.x - self.B.pos.x)
    
    def getFunction(self, x):
        if (self.A.pos.x - self.B.pos.x) != 0:
            m = self.getGradient()
            c = self.B.pos.y - m * self.B.pos.x
            return m * x + c
    
    def cut(self):
        mouse = pygame.mouse
        if mouse.get_pressed()[0] & (self.getFunction(mouse.get_pos()[0]) == mouse.get_pos()[1]):
            print("cut")
        

        