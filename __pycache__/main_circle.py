import pygame
from block import Block

class Main_circle():
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.circle_img = pygame.Surface((radius, radius), pygame.SRCALPHA)
        self.circle_img_rect =  self.circle_img.get_rect()
        self.color = (255, 0, 0)
                
    def move(self, block):
        self.x = block.rect_x + 31
        self.y = block.rect_y
        lst = list(self.color)
        lst[0] = lst[0] ^ 255
        lst[2] = lst[2] ^ 255
        self.color = tuple(lst)
    
    def draw(self, screen):
        screen.blit(self.circle_img, (self.x, self.y))
        pygame.draw.circle(self.circle_img, self.color, (self.radius//2, self.radius//2), self.radius//2)

class Orbit():        
    def __init__(self, screen, x, y, radius, outline):
        self.x = x
        self.y = y
        self.radius = radius
        self.oitline = outline
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), radius, outline)