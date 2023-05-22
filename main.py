import pygame
import sys
import random


#Constant and variables
SIZE = (1440, 900) #Screen size
FPS = 60 
i=0 # This is to index the Colors
speed = [2 for _ in range(2)] # list of speeds
colors = ['Blue', 'Orange', 'Purple', 'Yellow', 'Red', 'Green', 'Pink'] # list of logo colors

# Initialize Pygame & Set the dimension of the window
pygame.init()
screen =  pygame.display.set_mode((SIZE))
pygame.display.set_caption('Bouncing DVD By EL ATIK')
clock = pygame.time.Clock()


def logo_color(i):
    # this fuction return a logo with a color
    color = colors[i]
    logo = pygame.image.load(f"Logos\\{color}.jpg").convert_alpha()
    logo_size = [1450,680]
    for i in range(2):
        logo_size[i] = logo_size[i] /5
    logo = pygame.transform.scale(logo,(logo_size[0],logo_size[1])).convert_alpha()
    return logo


logo = logo_color(i)
logo_rect = logo.get_rect(topleft=(0,0))


def text_position_random():
    text_x = random.randint(20,1280)
    text_y = random.randint(20, 880)
    return [text_x,text_y]
font = pygame.font.Font(None, 20)
text = font.render("Bouncing DVD By Elatik", None, "grey")
text_rect = text.get_rect(topleft=text_position_random())


while True:
    # This is the game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Check if the logo hits the edges of the screen
    if logo_rect.left < 0 or logo_rect.right > SIZE[0]:
        if i < 6:
            i += 1
        else:
            i =0
        speed[0] = -speed[0]
        logo = logo_color(i)
        
    if logo_rect.top < 0 or logo_rect.bottom > SIZE[1]:
        if i < 6:
            i += 1
        else:
            i =0
        speed[1] = -speed[1]
        logo = logo_color(i)
    
    # Update the position of the logo
    logo_rect.x += speed[0]
    logo_rect.y += speed[1]
    if logo_rect.x % 100 ==0:
        text_rect = text.get_rect(topleft=text_position_random())
    
    # Fill the screen with black color
    screen.fill('black') 
    
    # Draw the logo on the screen
    screen.blit(logo, logo_rect)
    screen.blit(text, text_rect)
    # Update the display
    pygame.display.update() 
    # Limit the frame rate to 60 FPS
    clock.tick(FPS) 