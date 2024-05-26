from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_height, player_width, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_height, player_width))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.height = player_height
        self.width = player_width
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            self.rect.y -= self.speed
        if keys_pressed[K_s]:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP]:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN]:
            self.rect.y += self.speed


racket1 = Player('racket.png', 50, 200, 30, 100, 4)
racket2 = Player('racket2.png', 650, 200, 30, 100, 4)
ball = GameSprite('ball.png', 325, 225, 50, 50, 2)
win_height = 700
win_wigth = 500
clock = time.Clock()
window = display.set_mode((win_height, win_wigth))
back = (0, 128, 128)
window.fill(back)
display.set_caption("Пинг-понг")
font.init()
font1 = font.SysFont('Arial', 36)

speed_x = 3
speed_y = 3
Game = True
Finish = False
while Game:
    for e in event.get():
        if e.type == QUIT:
            Game = False
    if Finish != True:
        window.fill(back)
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        lose1 = font1.render("ПРОИГРЫШ 1 ИГРОКА", 1, (255, 0, 0))
        lose2 = font1.render("ПРОИГРЫШ 2 ИГРОКА", 1, (255, 0, 0))
        racket1.update1()
        racket2.update2()
        racket1.reset()
        racket2.reset()
        ball.reset()
    if ball.rect.y > win_wigth-50 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1
    if ball.rect.x < 0:
        window.blit(lose1, (150, 200))
        finish = True
    if ball.rect.x > 650:
        window.blit(lose2, (150, 200))
        finish = True
    clock.tick(60)
    display.update()