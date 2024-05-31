from particle import *
from chord import *
import math

class Physics:
    def __init__(self, screen, fps, gravity_dir=(0, 1), bounds=[], pxpm=100) -> None:
        self.bodies=[]
        self.gravity_dir=gravity_dir
        self.fps = fps
        self.screen = screen
        self.bounds = bounds # [x1, x2, y1, y2]
        self.pxpm = pxpm # 1 meter = 100 px
        self.g = 9.8 * self.pxpm / math.pow(self.fps, 2) #9.8 * self.pxpm / 3780 / math.pow(self.fps, 2)

    def update(self):
        for body in self.bodies:
            body.draw(self.screen)
            if type(body)==Chord:
                body.pull(self.pxpm)
            if type(body)==Particle:
                self.bounds_collision(body)
                self.apply_gravity(body)


    def add(self, *bodies):
        for body in bodies:
            self.bodies.append(body)

    def bounds_collision(self, particle):
        # left wall
        if (particle.pos.x <= self.bounds[0]):
            error = self.bounds[0] - particle.pos.x # how much further did the particle fall than the bounds before it got constrained
            particle.vel.x = -particle.vel.x - error / 100 * particle.elasticity

        # right wall
        if (particle.pos.x >= self.bounds[1]):
            error = self.bounds[1] - particle.pos.x # how much further did the particle fall than the bounds before it got constrained
            particle.vel.x = -particle.vel.x - error / 100 * particle.elasticity

        # ceiling
        if (particle.pos.y <= self.bounds[2]): 
            error = self.bounds[2]-particle.pos.y # how much further did the particle fall than the bounds before it got constrained
            particle.vel.y = -particle.vel.y - error / 100 * particle.elasticity
            particle.apply_force(pygame.math.Vector2(0, -self.g)) # normal force
            print()
            print("bounce")
            print()
        
        # floor
        if (particle.pos.y >= self.bounds[3]):
            error = self.bounds[3]-particle.pos.y # how much further did the particle fall than the bounds before it got constrained
            particle.vel.y = -particle.vel.y - error / 100 * particle.elasticity
            particle.apply_force(pygame.math.Vector2(0, -self.g)) # normal force
            print()
            print("bounce")
            print()

        # constrain
        particle.pos.x = max(self.bounds[0], min(particle.pos.x, self.bounds[1]))
        particle.pos.y = max(self.bounds[2], min(particle.pos.y, self.bounds[3]))

    
    def apply_gravity(self, particle):
        gravitational_force = pygame.math.Vector2(0, self.g)
        particle.apply_force(gravitational_force)