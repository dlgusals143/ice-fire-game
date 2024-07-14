import pygame

gray = (128, 128, 128)




# 블록 객체
class Block():
    def __init__(self, screen, rect_x, rect_y, rect_width, rect_height):
        self.rect_x = rect_x
        self.rect_y = rect_y
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.screen = screen
        self.color = (255, 255, 255) 
        
    def draw(self):
        pygame.draw.rect(self.screen, gray, (self.rect_x, self.rect_y, self.rect_width, self.rect_height))
        pygame.draw.rect(self.screen, self.color, (self.rect_x+3, self.rect_y+4, self.rect_width-9, self.rect_height-9))
        
    def update(self):
        self.rect_x += 5
        