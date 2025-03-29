import pygame
import os
import random

VEL = 5
WIDTH,HEIGHT = 900,900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
FPS = 60 #frames per second

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40

pygame.display.set_caption("Shoot the blocks")

class SpaceShip():
    def __init__(self, img, rotation, dimension):
        a_surf = pygame.image.load(os.path.join('Assets', img))
        self.surface = pygame.transform.rotate(pygame.transform.scale(a_surf,dimension,),rotation)
        self.x = WIDTH/2
        self.y = HEIGHT -100

    def updateX(self, x_diff):
        self.x += x_diff

    def updateY(self, y_diff):
        self.y += y_diff


#load a new image from a file "spaceship_yellow.png" using pygame.image.load

os.chdir("/Users/CFF/Downloads")
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
ASTEROID_IMAGE = pygame.image.load(os.path.join('Assets', 'asteroid.png'))

#create a new surface for this image using pygame.Surface.convert_alpha

# rotate this image and scale it using pygame.transform 
YELLOW_SPACESHIP = SpaceShip('spaceship_yellow.png',180,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

#define a draw_window function that displays all elements on the screen
def draw_window():
    pygame.draw.rect(WIN, BLACK, pygame.Rect(0,0,WIDTH,HEIGHT))
    WIN.blit(YELLOW_SPACESHIP.surface, (YELLOW_SPACESHIP.x, YELLOW_SPACESHIP.y))
    WIN.blit(pygame.transform.scale(ASTEROID_IMAGE,(50,50)),(WIDTH/2,HEIGHT/2))
    
    
    # Display the YELLOW_SPACESHIP surface using pygame.surface.blit
    #     
asteroids = []
# asteroids.append(Asteroid('asteroid.png', (50,50))) 
# ADD ASTEROID CLASS FOR ASTEROIDS

   
game_running = True
while game_running:
    clock = pygame.time.Clock()
    clock.tick(FPS)
    #check for all the events that can occur
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_running = False

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        if YELLOW_SPACESHIP.x > VEL:
            YELLOW_SPACESHIP.updateX(0-VEL)
        
    if keys_pressed[pygame.K_RIGHT]:
        if YELLOW_SPACESHIP.x < WIDTH - SPACESHIP_WIDTH - VEL:
            YELLOW_SPACESHIP.updateX(VEL)
    
    draw_window()

    pygame.display.update()
    


    
    

pygame.quit()