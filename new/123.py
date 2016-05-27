import pygame

window = pygame.display.set_mode((780,600))
pygame.display.set_caption('bombser')

screen = pygame.Surface((780,600))
info_string = pygame.Surface((780,90))

class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x=xpos
        self.y=ypos
        self.bitmap=pygame.image.load(filename)
        self.bitmap.set_colorkey((0,0,0))
    def render(self):
        screen.blit(self.bitmap, (self.x,self.y))

class Hero:
    def __init__(self, team, x, y, filename, bomb):
        self.sprite = Sprite(x,y,filename)
        self.team = team
        self.left = True
        self.right = True
        self.up = True
        self.down = True
        self.keys = (pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN,pygame.K_RSHIFT,pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s,pygame.K_q)
        self.bomb = bomb
        self.z = 'd'
        self.score = 0
    def render(self):
        self.sprite.render()
    def move(self,keys):
        if keys[self.keys[self.team*4 + self.team]]:
            if ((self.left == True) and (self.sprite.x > 30)):
                self.sprite.x -= 10
                if self.bomb.move == False:
                    self.z = 'a'
        self.left = True
        if keys[self.keys[self.team*4 + 1 + self.team]]:
            if ((self.right == True) and (self.sprite.x < 720)) :
                self.sprite.x += 10
                if self.bomb.move == False:
                    self.z = 'd'
        self.right = True
        if keys[self.keys[self.team*4 + 2 + self.team]]:
            if ((self.up == True) and (self.sprite.y > 120)):
                self.sprite.y -= 10
                if self.bomb.move == False:
                    self.z = 'w'
        self.up = True
        if keys[self.keys[self.team*4 + 3 + self.team]]:
            if ((self.down == True) and (self.sprite.y < 540)):
                self.sprite.y += 10
                if self.bomb.move == False:
                    self.z = 's'
        self.down = True
        if keys[self.keys[self.team*4 + 4 + self.team]]:
            if self.bomb.push == False:
                if self.z == 'a':
                    self.bomb.sprite.x = self.sprite.x - 30
                    self.bomb.sprite.y = self.sprite.y
                if self.z == 'd':
                    self.bomb.sprite.x = self.sprite.x + 30
                    self.bomb.sprite.y = self.sprite.y
                if self.z == 'w':
                    self.bomb.sprite.x = self.sprite.x
                    self.bomb.sprite.y = self.sprite.y - 30
                if self.z == 's':
                    self.bomb.sprite.x = self.sprite.x
                    self.bomb.sprite.y = self.sprite.y + 30
                self.bomb.push = True
                self.bomb.move = True
                self.bomb.time = 25

class Bomb:
    def __init__(self, x, y, filename):
        self.sprite = Sprite(x,y,filename)
        self.push = False
        self.move = False
        self.time = 25
    def render(self):
        self.sprite.render()
    def boom(self,hero):
        if self.time == 10:
            self.move = False
        if ((self.time > -5) and (self.time < 0)):
                fire = Sprite(self.sprite.x-30,self.sprite.y-30,'2.png')
                fire.render()
                if ((self.hero.sprite.x > self.sprite.x-60) and (self.hero.sprite.x < self.sprite.x+60) and (self.hero.sprite.y > self.sprite.y-60) and (self.hero.sprite.y < self.sprite.y+60)):
                    self.hero.sprite.x = 360
                    self.hero.sprite.y = 360
                    self.hero.score -= 1
                if ((hero.sprite.x > self.sprite.x-60) and (hero.sprite.x < self.sprite.x+60) and (hero.sprite.y > self.sprite.y-60) and (hero.sprite.y < self.sprite.y+60)):
                    hero.sprite.x = 360
                    hero.sprite.y = 360
                    self.hero.score += 1

        if self.time == -5:
            self.push = False
        if self.push == False:
            self.sprite.x = 780
            self.sprite.y = 510
        if self.move == True:
            if self.hero.z == 'a':
                self.sprite.x -= 25
            elif self.hero.z == 'd':
                self.sprite.x += 25
            elif self.hero.z == 'w':
                self.sprite.y -= 25
            if self.hero.z == 's':
                self.sprite.y += 25

        if (Intersect(self.hero.sprite.x, hero.bomb.sprite.x, self.hero.sprite.y, hero.bomb.sprite.y, 30) == True):
            hero.bomb.move = False


def Intersect (s1_x,s2_x,s1_y,s2_y,const):
    if ((s1_x>s2_x-const) and (s1_x<s2_x+const) and (s1_y>s2_y-const) and (s1_y<s2_y+const)):
        return 1
    else:
        return 0

def block(i,hero):
    if (Intersect(i.x,hero.bomb.sprite.x,i.y,hero.bomb.sprite.y,30) == True):
        hero.bomb.move = False
    if Intersect(i.x,hero.sprite.x,i.y,hero.sprite.y,31) == True:
        if (i.x > hero.sprite.x-31) and (i.x < hero.sprite.x-29):
            if ((((i.y > hero.sprite.y - 30)) and (i.y < hero.sprite.y + 29)) or ((i.y < hero.sprite.y + 30) and (i.y > hero.sprite.y + 29))):
                hero.left = False
                hero.right = True
                hero.up = True
                hero.down = True
        elif ((i.x < hero.sprite.x+31) and (i.x > hero.sprite.x+29)):
            if ((((i.y > hero.sprite.y - 30)) and (i.y < hero.sprite.y + 29)) or ((i.y < hero.sprite.y + 30) and (i.y > hero.sprite.y + 29))):
                hero.left = True
                hero.right = False
                hero.up = True
                hero.down = True
        elif ((i.y > hero.sprite.y-31) and (i.y < hero.sprite.y+29)):
            hero.left = True
            hero.right = True
            hero.up = False
            hero.down = True
        elif ((i.y < hero.sprite.y+31) and (i.y > hero.sprite.y+29)):
            hero.left = True
            hero.right = True
            hero.up = True
            hero.down = False

pygame.font.init()
score_font = pygame.font.Font(None,64)

bombs = Bomb(780,510,'3.png')
bomb = Bomb(780,510,'3.png')
heros = Hero(1,30,120,'4.png',bombs)
hero = Hero(0,720,540,'4.png',bomb)
bombs.hero = heros
bomb.hero = hero

bombs.time = -10
bomb.time = -10
done = True

while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

    pressed = pygame.key.get_pressed()
    heros.move(pressed)
    hero.move(pressed)
    bombs.time -= 1
    bomb.time -=1

    screen.fill((50, 50, 50))
    info_string.fill((20,0,20))

    blocks1 = []
    blocks = []
    for i in range(0, 780, 30):
        blocks1.append(Sprite(i, 90, '1.png'))
        blocks1.append(Sprite(i, 570, '1.png'))
    for i in range(90, 570, 30):
        blocks1.append(Sprite(0, i, '1.png'))
        blocks.append(Sprite(90, 3*i-120, '1.png'))
        blocks.append(Sprite(180, 3*i-120, '1.png'))
        blocks.append(Sprite(270, 3*i-120, '1.png'))
        blocks1.append(Sprite(750, i, '1.png'))
    for i in blocks1:
        if (Intersect(i.x, bombs.sprite.x, i.y, bombs.sprite.y,30) == True):
            bombs.move = False
        if (Intersect(i.x, bomb.sprite.x, i.y, bomb.sprite.y,30) == True):
            bomb.move = False
        i.render()
    for i in blocks:
        block(i,hero)
        block(i,heros)
        i.render()

    bombs.render()
    heros.render()
    bomb.render()
    hero.render()

    bombs.boom(hero)
    bomb.boom(heros)

    info_string.blit(score_font.render('P1: '+str(heros.score),1,(210,120,200)),(20,20))
    info_string.blit(score_font.render('P2: '+str(hero.score),1,(210, 120, 200)),(420, 20))
    window.blit(screen,(0,0))
    window.blit(info_string, (0, 0))

    pygame.display.flip()


