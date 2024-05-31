import pygame.draw
import pygame.mouse
import pygame.math
import random

class Particle:
    def __init__(self, x, y, radius=10, fixed=False, colour=(0, 0, 0), elasticity=1) -> None:
        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0.0, 0.0)
        self.clicked = False
        self.fixed = fixed
        self.path = []
        self.radius = radius
        self.colour = (random.randrange(50, 255), random.randrange(50, 255), random.randrange(50, 255))
        self.forces = []
        self.elasticity = elasticity
        

    def apply_force(self, vec):
        self.forces.append(vec)

    def determine_net_force(self):
        net = pygame.math.Vector2(0, 0)
        for force in self.forces:
            net += force
        return net

    def _move(self):    
        mouse = pygame.mouse
        self._click()
        
        if self.clicked:
            self.vel = mouse.get_rel()
            self.pos += self.vel
            
        elif not self.fixed:
            self.vel += self.determine_net_force()
            self.pos += self.vel
        
        self.forces = []



    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.pos, self.radius)
        # self.path.append([self.pos[0], self.pos[1]])
        if len(self.path) >= 2:
            pygame.draw.lines(screen, (0, 200, 0), False, self.path)
        self._move()
        

    def _click(self):
        mouse = pygame.mouse
        
        if (self.pos[0] - self.radius) <= mouse.get_pos()[0] <= self.pos[0] + self.radius:
            if (self.pos[1] - self.radius) <= mouse.get_pos()[1] <= (self.pos[1] + self.radius):
                if mouse.get_pressed()[0]:
                    self.clicked = True

        if not mouse.get_pressed()[0]:
            self.clicked = False;