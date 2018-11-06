import pygame
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.move = True
        self.image = pygame.Surface((20,20),pygame.SRCALPHA)
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.edge = False
        self.stop = False
        self.rect.midbottom = (x, y)
        self.currentspeed = 2
    def update(self):
        if not self.stop:
            if not self.edge:
                self.rect.x += self.currentspeed
            else:
                self.rect.x -= self.currentspeed
        if self.stop:
            None
