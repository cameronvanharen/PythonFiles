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



asteroid_spawn_time = 0
asteroid_frequency = 30

pygame.display.set_caption("Shoot the blocks")

class SpaceShip():
    def __init__(self, img, rotation, dimension):
        a_surf = pygame.image.load(os.path.join('Assets', img))
        self.surface = pygame.transform.rotate(pygame.transform.scale(a_surf,dimension,),rotation)
        self.rect = pygame.Rect(0, HEIGHT-100, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
       
    def updateX(self, x_diff):
        self.rect.x += x_diff

    def updateY(self, y_diff):
        self.rect.y += y_diff

asteroid_surf = pygame.Surface.convert_alpha(pygame.image.load(os.path.join('Assets', 'Asteroid.png')))

class Asteroid():
    def __init__(self, img, dimension):
        self.surface = pygame.transform.scale(asteroid_surf, dimension)
        self.rect = pygame.Rect(random.randint(0,WIDTH), 0, dimension[0], dimension[1])
        self.velocity = 10

    def updateX(self, x_diff):
            self.rect.x += x_diff

    def updateY(self, y_diff):
            self.rect.y += y_diff



#load a new image from a file "spaceship_yellow.png" using pygame.image.load

os.chdir("/Users/cff/Documents/Python")
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
ASTEROID_IMAGE = pygame.image.load(os.path.join('Assets', 'asteroid.png'))

#create a new surface for this image using pygame.Surface.convert_alpha

# rotate this image and scale it using pygame.transform 
YELLOW_SPACESHIP = SpaceShip('spaceship_yellow.png',180,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

asteroids = []
collideTimes = 0

#define a draw_window function that displays all elements on the screen
def draw_window():
    pygame.draw.rect(WIN, BLACK, pygame.Rect(0,0,WIDTH,HEIGHT))
    WIN.blit(YELLOW_SPACESHIP.surface, (YELLOW_SPACESHIP.rect.x, YELLOW_SPACESHIP.rect.y))
    for ast in asteroids:
        WIN.blit(ast.surface, (ast.rect.x, ast.rect.y))

def is_Ship_Hit(list_asteroids, ship_rect):
    for ast in list_asteroids:
       if ship_rect.colliderect(ast.rect):
           list_asteroids.remove(ast)
           return True
    return False
    
    
    # Display the YELLOW_SPACESHIP surface using pygame.surface.blit
    #     

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
        if YELLOW_SPACESHIP.rect.x > VEL:
            YELLOW_SPACESHIP.updateX(0-VEL)
        
    if keys_pressed[pygame.K_RIGHT]:
        if YELLOW_SPACESHIP.rect.x < WIDTH - SPACESHIP_WIDTH - VEL:
            YELLOW_SPACESHIP.updateX(VEL)

    for ast in asteroids:
        if(ast.rect.y > HEIGHT):
            asteroids.remove(ast)
        else:
            ast.updateY(ast.velocity)

    ticks = pygame.time.get_ticks()
    if ticks - asteroid_spawn_time > asteroid_frequency:
        asteroid_spawn_time = ticks
        asteroids.append(Asteroid('asteroid.png',(random.randint(40,60),50)))
    
    if is_Ship_Hit(asteroids, YELLOW_SPACESHIP.rect):
        print("collide" + str(collideTimes))
        collideTimes += 1


    draw_window()

    pygame.display.update()
    


    
    

pygame.quit()