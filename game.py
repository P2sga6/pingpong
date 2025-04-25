from pygame import *

wi = display.set_mode((971, 490))
display.set_caption('ping pong')
background = transform.scale(image.load('Screenshot_11.png'), (971, 490))

game = True
while game:
    wi.blit(background(0, 0))
    display.update()