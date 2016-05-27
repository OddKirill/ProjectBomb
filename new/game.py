import pygame

window = pygame.display.set_mode((780,600))
pygame.display.set_caption('Bomber')

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

def Intersect (s1_x,s2_x,s1_y,s2_y,const):
    if ((s1_x>s2_x-const) and (s1_x<s2_x+const) and (s1_y>s2_y-const) and (s1_y<s2_y+const)):
        return 1
    else:
        return 0

pygame.font.init()
score_font = pygame.font.Font(None,64)

hero = Sprite(360,360,'1.png')
hero2 = Sprite(580,360,'1.png')
bomb = Sprite(780,510,'3.png')
bomb2 = Sprite(780,510,'3.png')

bomb.push = False
bomb.move = False
hero.left = True
hero.right = True
hero.up = True
hero.down = True
bomb2.push = False
bomb2.move = False
hero2.left = True
hero2.right = True
hero2.up = True
hero2.down = True

time = -10
time2 = -10
z = 'd'
z2 = 'LEFT'
score1 = 0
score2 = 0
pygame.key.set_repeat(1,1)

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            if ((hero.left == True) and (hero.x > 30)):
                hero.x -= 10
                if bomb.move == False:
                    z = 'a'
        hero.left = True
        if pressed[pygame.K_d]:
            if ((hero.right == True) and (hero.x < 720)) :
                hero.x += 10
                if bomb.move == False:
                    z = 'd'
        hero.right = True
        if pressed[pygame.K_w]:
            if ((hero.up == True) and (hero.y > 120)):
                hero.y -= 10
                if bomb.move == False:
                    z = 'w'
        hero.up = True
        if pressed[pygame.K_s]:
            if ((hero.down == True) and (hero.y < 540)):
                hero.y += 10
                if bomb.move == False:
                    z = 's'
        hero.down = True
        if pressed[pygame.K_q]:
            if bomb.push == False:
                if z == 'a':
                    bomb.x = hero.x - 30
                    bomb.y = hero.y
                if z == 'd':
                    bomb.x = hero.x + 30
                    bomb.y = hero.y
                if z == 'w':
                    bomb.x = hero.x
                    bomb.y = hero.y - 30
                if z == 's':
                    bomb.x = hero.x
                    bomb.y = hero.y + 30
                    bomb.push = True
                    bomb.move = True
                    time = 25

    time -= 1
    time2 -= 1

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
        if (Intersect(i.x, bomb.x, i.y, bomb.y,30) == True):
            bomb.move = False
        if (Intersect(i.x, bomb2.x, i.y, bomb2.y, 30) == True):
            bomb2.move = False
        i.render()
    for i in blocks:
        if (Intersect(i.x,bomb.x,i.y,bomb.y,30) == True):
            bomb.move = False
        if (Intersect(i.x, bomb2.x, i.y, bomb2.y, 30) == True):
            bomb2.move = False
        if Intersect(i.x,hero.x,i.y,hero.y,31) == True:
            if (i.x > hero.x-31) and (i.x < hero.x-29):
                if ((((i.y > hero.y - 30)) and (i.y < hero.y + 29)) or ((i.y < hero.y + 30) and (i.y > hero.y + 29))):
                    hero.left = False
                    hero.right = True
                    hero.up = True
                    hero.down = True
            elif ((i.x < hero.x+31) and (i.x > hero.x+29)):
                if ((((i.y > hero.y - 30)) and (i.y < hero.y + 29)) or ((i.y < hero.y + 30) and (i.y > hero.y + 29))):
                    hero.left = True
                    hero.right = False
                    hero.up = True
                    hero.down = True
            elif ((i.y > hero.y-31) and (i.y < hero.y+29)):
                hero.left = True
                hero.right = True
                hero.up = False
                hero.down = True
            elif ((i.y < hero.y+31) and (i.y > hero.y+29)):
                hero.left = True
                hero.right = True
                hero.up = True
                hero.down = False



        i.render()

    bomb.render()
    hero.render()

    if time == -5:
        bomb.push = False
    if bomb.push == False:
        bomb.x = 780
        bomb.y = 510
    if bomb.move == True:
        if z == 's':
            bomb.y += 25
        if z == 'a':
            bomb.x -= 25
        if z == 'd':
            bomb.x += 25
        if z == 'w':
            bomb.y -= 25




    info_string.blit(score_font.render('P1: '+str(score1),1,(210,120,200)),(20,20))
    info_string.blit(score_font.render('P2: '+str(score2),1,(210, 120, 200)),(420,20))
    window.blit(screen,(0,0))
    window.blit(info_string,(0, 0))

    pygame.display.flip()


