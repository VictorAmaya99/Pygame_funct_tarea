import pygame
from config import *
import math 

figures = [
            {"type": "circle", "drawing": pygame.draw.circle, "color": GREEN, "position":(400,300), "radius": 110},
            {"type": "rectangle", "drawing": pygame.draw.rect, "color": GREEN, "position": (280, 220, 250, 150)},
            {"type": "square", "drawing": pygame.draw.rect, "color":GREEN, "position": (290, 200, 200, 200)},
            {"type": "polygon", "drawing": pygame.draw.polygon, "color":GREEN, "position": [(300, 200), (500,400), (300,400)]}]

def draw_circle(lista=list, surface=0):
    for fig in lista:
        type = fig["type"]
        if type == "circle":
            fig["drawing"](surface, fig["color"], fig["position"], fig["radius"])

def draw_rectangle(lista=list, surface=0):
    for fig in lista:
        type = fig["type"]
        if type == "rectangle":
            fig["drawing"](surface, fig["color"], fig["position"])

def draw_square(lista=list, surface=0):
    for fig in lista:
        type = fig["type"]
        if type == "square":
            fig["drawing"](surface, fig["color"], fig["position"])

def draw_polygon(lista=list, surface=0):
    for fig in lista:
        type = fig["type"]
        if type == "polygon":
            fig["drawing"](surface, fig["color"], fig["position"])

def circle_calculates(lista=list):
    for fig in lista: 
        radius = float(fig["radius"])   
        area = math.pi * (radius ** 2)
        perimeter = 2 * radius * math.pi
        return print (f"el perimetro es: {perimeter:5.2f} y el area es:{area:5.2f}")            
            
def rectangle_calculates(lista=list):
    for fig in lista:
        type = fig["type"]
        if type == "rectangle":
            width = float(fig["position"][2])    
            height = float(fig["position"][3] )  
            area = width * height
            perimeter = (width*2) + (height*2)    
            return print(perimeter, area)

def square_calculates(lista=list):
    for fig in lista:
        type = fig["type"]
        if type == "square":
            width = float(fig["position"][2])     
            height = float(fig["position"][3])
            area = width * height
            perimeter = (width*2) + (height*2)    
            return print(perimeter, area)
        
def polygon_calculates(lista=list):
    for fig in lista:
        type = fig["type"]    
        if type == "polygon":
            x1 = float(fig["position"][0][0])
            y1 = float(fig["position"][0][1])
            x2 = float(fig["position"][1][0])
            y2 = float(fig["position"][1][1])
            x3 = float(fig["position"][2][0])
            y3 = float(fig["position"][2][1])
            area = 1/2 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
            perimeter = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))    
            return print(perimeter, area)

def write_circle_calculations(surface=0):
    font = pygame.font.SysFont("Arial", 40)
    text1 = font.render("Perimetro: 691.15 px", False, GREEN, LIGHT_BLUE)
    text2 = font.render("Area: 38013.27 px", False, GREEN, LIGHT_BLUE)
    surface.blit(text1, (0,500))
    surface.blit(text2, (0,550))
    return text1, text2

def write_rectangule_calculations(surface=0):
    font = pygame.font.SysFont("Arial", 40)
    text1 = font.render("Perimetro: 800.00 px", False, GREEN, LIGHT_BLUE)
    text2 = font.render("Area: 37500.00 px", False, GREEN, LIGHT_BLUE)
    surface.blit(text1, (0,500))
    surface.blit(text2, (0,550))
    return text1, text2

def write_square_calculations(surface=0):
    font = pygame.font.SysFont("Arial", 40)
    text1 = font.render("Perimetro: 800.00 px", False, GREEN, LIGHT_BLUE)
    text2 = font.render("Area: 40000.00 px", False, GREEN, LIGHT_BLUE)
    surface.blit(text1, (0,500))
    surface.blit(text2, (0,550))
    return text1, text2

def write_polygon_calculations(surface=0):
    font = pygame.font.SysFont("Arial", 40)
    text1 = font.render("Perimetro: 40000.00 px", False, GREEN, LIGHT_BLUE)
    text2 = font.render("Area: 20000.00 px", False, GREEN, LIGHT_BLUE)
    surface.blit(text1, (0,500))
    surface.blit(text2, (0,550))
    return text1, text2



