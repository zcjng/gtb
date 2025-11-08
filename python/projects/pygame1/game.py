
import pygame
import math
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Knight(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(os.path.join(BASE_DIR, 'assets/knight.png')).convert()
        self.image.set_colorkey((99, 155, 255))
        self.rect = self.image.get_rect(center=pos)
        self.vector = (0, 0)
        self.vx = 0
        self.vy = 0
        self.gravity = 0.5
        self.on_ground = False
        self.jump_power = -10
        
    def self_gravity(self):
        self.vy += self.gravity
        self.rect.y += self.vy
    
    def jump(self):
        if self.on_ground:
            self.vy = self.jump_power
            self.on_ground = False
        
    def check_collision(self, ground):
        if self.rect.colliderect(ground.rect):
            if self.vy > 0:
                self.rect.bottom = ground.rect.top
                self.vy = 0
                self.on_ground = True
        else:
            self.on_ground = False

        
    def update(self):
        newpos = self.calcnewpos(self.rect, self.vector)
        self.rect = newpos
        
    def calcnewpos(self, rect, vector):
        (angle, z) = vector
        (dx, dy) = (z * math.cos(angle), z * math.sin(angle))
        return rect.move(dx, dy)
    
class Ground(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(os.path.join(BASE_DIR, 'assets/ground.jpg')).convert()
        self.rect = self.image.get_rect(topleft=pos)
        self.vector = (0, 0)
        self.image = pygame.transform.scale(self.image, (1280, 200))

        
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
dt = 0

pygame.display.set_caption('Mario Knight')
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
knight = Knight(player_pos)
ground = Ground((0, 600))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
   
    if keys[pygame.K_a]:
        knight.rect.x -= 300 * dt

    if keys[pygame.K_d]:
        knight.rect.x += 300 * dt
    
    if keys[pygame.K_SPACE] or keys[pygame.K_w]:
        knight.jump()
    
    knight.self_gravity()
    knight.check_collision(ground)
    
    background = pygame.Surface(screen.get_size())
    background.fill('skyblue')
    

    
    
    #render
    
    font = pygame.font.Font(None, 30)
    text = font.render('This is the mario knight', 1, (10,10,10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)
    background.blit(knight.image, knight.rect)
    background.blit(ground.image, ground.rect)
    
    screen.blit(background, (0,0))
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000
    
pygame.quit()