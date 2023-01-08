from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    #class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__() #sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        #every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    #method drawing the character on the window
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#child class
class Paddle (GameSprite):
    #method to control the sprite with arrow keys
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

#interface
BLACK = (13, 12, 12)
win_width = 800
win_height = 700
window = display.set_mode((win_width, win_height))
window.fill(BLACK)


#create sprites (paddle and balls)
paddleA_img = "paddle1.png"
paddleB_img = "paddle2.png"
ball_img = "ball.png"

paddleA = Paddle (paddleA_img, 20, 200, 30, 150, 10)
paddleB = Paddle (paddleB_img, 750, 200, 30, 150, 10)
ball = GameSprite(ball_img, 330, 200, 50, 50, 50)


#game loop
game = True
finish = False
clock = time.Clock()
FPS = 60

#fonts
font.init()
font = font.Font("pdark.ttf", 35)
lose1 = font.render('PLAYER 1 LOST!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOST!', True, (180, 0, 0))

speed_x = 7
speed_y = 7

while game:
    for e in event.get():
        if e.type ==QUIT:
            game = False

    if finish != True:
        window.fill (BLACK)
        paddleA.update_left()
        paddleB.update_right()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(paddleA, ball) or sprite.collide_rect(paddleB, ball):
            speed_x *= -1
            speed_y *= 1

        #ball bounces when hit the up or bottom wall
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        #if ball flies behind this paddle, display loss condition for player left
        if ball.rect.x < 0:
            finish = False
            window.blit(lose1, (200, 200))

        #if the ball flies behind this paddle, display loss condition for player right
        if ball.rect.x > win_width:
            finish = False
            window.blit(lose2, (200, 200))

        paddleA.reset()
        paddleB.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)