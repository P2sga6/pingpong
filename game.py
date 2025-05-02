from pygame import *
from random import randint

window = display.set_mode((972, 490))
display.set_caption('Ping Pong')
background = transform.scale(image.load('Screenshot_11.png'), (972, 490))

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (90, 90))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 440:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 440:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        if self.rect.y >= 500:
            self.rect.x = randint(60, 500)
            self.rect.y = 0
        self.rect.y += self.speed


    
player = Player('racket1.png', 2, 25, 200)
player2 = Player2('racket2.png', 2, 870, 200)
ball = Ball('ball.png', 2, 50, 400)


game = True
while game:
    window.blit(background,(0,0))
    clock.tick(FPS)

    player.update()
    player2.update()
    ball.update()
    player.reset()
    player2.reset()
    ball.reset()

    for e in event.get():
        if e.type == QUIT:
            game = False


    display.update()

