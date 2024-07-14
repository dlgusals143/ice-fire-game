import pygame
import math

class Sub_circle():
    def __init__(self, screen, radius, orbit):
        self.x = orbit.x
        self.y = orbit.y + orbit.radius
        self.screen = screen
        print(self.x, self.y)
        self.radius = radius
        self.orbit= orbit
        self.angle = 156
                
        self.color = (0, 0, 255)
        
        
    def move(self, block):
        self.orbit.x = block.rect_x + 60
        self.angle = 180
        lst = list(self.color)
        lst[0] = lst[0] ^ 255
        lst[2] = lst[2] ^ 255
        self.color = tuple(lst)
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        self.x = self.orbit.x + self.orbit.radius * math.cos(math.radians(self.angle))
        self.y = self.orbit.y + self.orbit.radius * math.sin(math.radians(self.angle))
        self.update()
        #print("angle", self.angle)
    
    def update(self):
        self.angle += 6
        if self.angle >= 360:
            self.angle = 0
            
#             # 게임 루프
# running = True

# while running:
#     # 원 업데이트
#     orbiting_circle.update()

#     # 원 그리기
#     orbiting_circle.draw(screen)

#     # 화면 업데이트
#     pygame.display.update()