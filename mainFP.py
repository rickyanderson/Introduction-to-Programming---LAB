from playerFP import *
from settingsFP import *

class Program():
    def __init__(self):
        pygame.init() #calling pygame
        pygame.mixer.init() #to add music
        self.screen = pygame.display.set_mode((screen_width, screen_height)) #Resolution
        self.clock = pygame.time.Clock()
        self.running = True
        self.play = True
        self.all_sprites = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.i = 0
        self.new_done = False

    def run(self):
        self.new()
        while self.play:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()

    def new(self):
        for block in blocklist[0]:
            b = Player(*block)
            self.all_sprites.add(b)
            self.blocks.add(b)

    def update(self):
        self.all_sprites.update()
        for block in self.blocks:
            if block.rect.x < 0 :
                for block in self.blocks:
                    block.edge = False
            if block.rect.x >= screen_width -20:
                for block in self.blocks:
                    block.edge = True
        if self.new_done:
            for newblock in blocklist[self.i]:
                b = Player(*newblock)
                self.all_sprites.add(b)
                self.blocks.add(b)
            self.new_done = False

    def event(self):
        for event in pygame.event.get(): #harus ada
            if event.type == pygame.QUIT:
                if self.play:
                    self.play = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.i += 1
                    self.new_done = True
                    for i in self.blocks:
                        i.stop = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    for i in self.blocks:
                        i.currentspeed += 2
                    None
            self.update()


    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()



