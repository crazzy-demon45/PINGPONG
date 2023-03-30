from pygame import *

win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))


class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed




back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


game = True
finish = False
clock = time.Clock()
FPS = 60
ball = GameSprite('tenis_ball.png', 200,200,5,50,50)
racket1 = Player('racket.png', 20, 100, 3, 50, 150)
racket2 = Player('racket.png', 530, 100, 3, 50, 150)

while game:

    for e in event.get():
         if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_r()
        racket2.update_l()
        ball.reset()
        racket1.reset()
        racket2.reset()



    display.update()
    clock.tick(FPS)
