import time
import pygame
import pygame.display
import pygame.draw
import pygame.mouse
import pygame.time 
from particle import *
from spring import *
from physics import *
import random

pygame.init() 

WIDTH, HEIGHT = 500, 500
FPS = 60

# CREATING CANVAS 
canvas = pygame.display.set_mode((WIDTH, HEIGHT)) 
clock = pygame.time.Clock()

# Physics
physics = Physics(canvas, FPS, bounds=[0, WIDTH, 0, HEIGHT], pxpm=100)

particleA1 = Particle(250.0, 100.0, elasticity=0.5)
particleA2 = Particle(300.0, 100.0, elasticity=0.5)
particleA3 = Particle(350.0, 100.0, elasticity=0.5)
particleB1 = Particle(250.0, 150.0, elasticity=0.5)
particleB2 = Particle(300.0, 150.0, elasticity=0.5)
particleB3 = Particle(350.0, 150.0, elasticity=0.5)
particleC1 = Particle(250.0, 150.0, elasticity=0.5)
particleC2 = Particle(300.0, 200.0, elasticity=0.5)
particleC3 = Particle(350.0, 200.0, elasticity=0.5)

# horisontal
physics.add(Chord(particleA1, particleA2))
physics.add(Chord(particleA2, particleA3))
physics.add(Chord(particleB1, particleB2))
physics.add(Chord(particleB2, particleB3))
physics.add(Chord(particleC1, particleC2))
physics.add(Chord(particleC2, particleC3))

#vertical
physics.add(Chord(particleA1, particleB1))
physics.add(Chord(particleA2, particleB2))
physics.add(Chord(particleA3, particleB3))
physics.add(Chord(particleB1, particleC1))
physics.add(Chord(particleB2, particleC2))
physics.add(Chord(particleB3, particleC3))

# diagonal
physics.add(Chord(particleA1, particleB2))
physics.add(Chord(particleA2, particleB3))
physics.add(Chord(particleB1, particleC2))
physics.add(Chord(particleB2, particleC3))


particleA1.fixed = True
particleA2.fixed = True
particleA3.fixed = True
particleC2.fixed = True
particleB1.fixed = True

physics.add(particleA1, particleA2, particleA3, particleB1, particleB2, particleB3, particleC1, particleC2, particleC3)
# physics.add(particleA1, particleA2, particleB1, particleB2)

# physics.add(chordBD)



# TITLE OF CANVAS 
pygame.display.set_caption("Physics") 
exit = False

mouse = pygame.mouse



i=1
while not exit: 

	canvas.fill((255, 255, 255))

	physics.update()

	mouse.get_rel()

	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			exit = True


	clock.tick(FPS)
	pygame.display.update() 
	i+=1