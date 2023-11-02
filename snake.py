import pygame
import random
from pygame.locals import (
	K_UP,
	K_DOWN,
	K_LEFT,
	K_RIGHT,
	K_q,
	KEYDOWN,
	QUIT,
)
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
direction = 0
x = int(SCREEN_WIDTH / 2)
y = int(SCREEN_HEIGHT / 2)
fillx = x
filly = y
running = True
fruit = False
restart = False
fx = 0
fy = 0
length = 1
dirlist = []
screen.fill((255,255,255))
while running:
	if restart:
		x = int(SCREEN_WIDTH / 2)
		y = int(SCREEN_HEIGHT / 2)
		fillx = x
		filly = y
		restart = False
		fruit = False
		length = 1
		dirlist = []
		direction = 0
		screen.fill((255,255,255))
		pygame.time.wait(800)
		pygame.event.clear()
	pygame.time.wait(200)
	changed = False
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_q):
            		running = False
		elif event.type == KEYDOWN and changed == False:
			if event.key == K_UP and direction != 3:
				direction = 1
			elif event.key == K_RIGHT and direction != 4:
				direction = 2
			elif event.key == K_DOWN and direction != 1:
				direction = 3
			elif event.key == K_LEFT and direction != 2:
				direction = 4
			changed = True
	dirlist.append(direction)
	if (fruit == False):
		fx = random.randrange(0, SCREEN_WIDTH / 50)*50
		fy = random.randrange(0, SCREEN_HEIGHT / 50)*50
		while (screen.get_at((fx,fy)).r == 0):
			fx = random.randrange(0, SCREEN_WIDTH / 50)*50
			fy = random.randrange(0, SCREEN_HEIGHT / 50)*50
		fruitsurf = pygame.Surface((20, 20))
		fruitsurf.fill((255,0,0))
		screen.blit(fruitsurf, (fx+15, fy+15))
		pygame.display.flip()
		fruit = True
	if (len(dirlist) > length):
		fillsurf = pygame.Surface((50,50))
		fillsurf.fill((255,255,255))
		if dirlist[0] == 1:
			filly = filly - 50
		elif dirlist[0] == 2:
			fillx = fillx + 50
		elif dirlist[0] == 3:
			filly = filly + 50
		elif dirlist[0] == 4:
			fillx = fillx - 50
		dirlist.pop(0)
		screen.blit(fillsurf, (fillx, filly))
		pygame.display.flip()
	surf = pygame.Surface((50,50))
	surf.fill((0,0,0))
	if direction == 1:
		y = y - 50
	elif direction == 2:
		x = x + 50
	elif direction == 3:
		y = y + 50
	elif direction == 4:
		x = x - 50
	if x == fx and y == fy:
		length = length + 1
		fruit = False
	if x < 0 or x >= SCREEN_WIDTH:
		restart = True
	elif y < 0 or y >= SCREEN_HEIGHT:
		restart = True
	elif running == True and screen.get_at((x,y)).r == 0 and direction != 0:
		restart = True
	screen.blit(surf, (x, y))
	pygame.display.flip()
pygame.quit()