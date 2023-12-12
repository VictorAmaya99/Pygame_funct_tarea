import pygame
from sys import exit
from module import *
from config import *
import math


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("TAREA")

background = pygame.image.load("Recursos/pizarra1.png")
back_scale = pygame.transform.scale(background, SCREEN_SIZE)
screen.blit(back_scale, (0,0))


is_running = True

while is_running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    
    
    draw_circle(figures, screen)
        
    write_circle_calculations(screen)

    pygame.display.flip()

    

pygame.quit()
exit()
    
