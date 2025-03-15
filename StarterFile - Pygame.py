import random
import pygame
from pygame.locals import *
import sys
pygame.init()
screen_width=700
screen_height=400

DISPLAYSURF=pygame.display.set_mode((400, 400))
pygame.display.set_caption("Hello Game!")

GREEN = (0,255,0)
RED = (255,0,0)
BLACK = (0,0,0)
WHITE=(255,255,255)
object1 = pygame.Rect((0,0),(20,20))

pygame.draw.rect(DISPLAYSURF, GREEN, object1)

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
       super().__init__()
       self.image = pygame.Surface([width,height])
       self.image.fill(color)
       self.image.set_colorkey(WHITE)

       pygame.draw.rect(self.image, color, [0,0,width,height])
       self.rect = self.image.get_rect()

block_list = pygame.sprite.Group()
for i in range(50):
    block = Block(BLACK, 20,15)

    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    block_list.add(block)

block_list.draw(DISPLAYSURF)
        




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            #sys.exit()
    DISPLAYSURF.fill(WHITE)
    block_list.draw(DISPLAYSURF)
    pygame.display.update()


      