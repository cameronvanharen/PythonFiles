import pygame
import random


# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Target properties
class Target:
    def __init__(self):
        self.color = (255,0,0)
        self.radius = 25
        self.x_pos = screen_width // 2
        self.y_pos = screen_height // 2


target_list = []

for i in range(0,10):
    target = Target()
    target.x_pos = random.randint(30,screen_width - 30)
    target.y_pos = random.randint(30,screen_height - 30)
    target.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    target.radius = random.randint(15,35)
    target_list.append(target)

score = 0
WHITE = (255,255,255)   

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf = largeText.render(text, True, WHITE)
    TextRect = TextSurf.get_rect()
    TextRect.center = (( screen_width/2),(screen_height/10))
    screen.blit(TextSurf, TextRect)

# Game loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for target in target_list:
                if (target.x_pos - mouse_x) **2 < target.radius **2 and (target.y_pos - mouse_y)**2 < target.radius **2:
                    print("Hit")
                    target.x_pos = random.randint(30, screen_width - 30)
                    target.y_pos = random.randint(30, screen_height - 30)
                    target.radius = random.randint(15,35)
                    target.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                    score += 1
                    print(score)
                
             
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw target
    for target in target_list:
        pygame.draw.circle(screen, target.color, (target.x_pos, target.y_pos), target.radius)
    # Update display
    message_display("score: " + str(score))
    pygame.display.flip()

# Quit Pygame
pygame.quit()