import pygame
import sys 
# initialisation 
pygame.init()
w_screen = 1280
h_screen  = 720

# Creat window
screen = pygame.display.set_mode((w_screen,h_screen))
clock = pygame.time.Clock()
running = True

bg = pygame.image.load('./img/bg-plage_night.png') 


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for x in range(0, w_screen, bg.get_width()):
        for y in range (0, h_screen, bg.get_height()):
            screen.blit(bg,(x,y))

 

    pygame.display.flip() #flip() ==> the display to put your work on screen    

    clock.tick(60) # limits 60fps
pygame.quit()
