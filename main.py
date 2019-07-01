import pygame as g
g.init()

#initialize console
win_width = 1200
win_height = 600
win = g.display.set_mode((win_width,win_height))
g.display.set_caption("Sample Game")

#images

#background
bg = g.image.load('bg.gif')

#player1
run_img_right_p1 = [g.image.load('Run (1).png'),g.image.load('Run (2).png'),g.image.load('Run (3).png'),
                    g.image.load('Run (4).png'),g.image.load('Run (5).png'),g.image.load('Run (6).png'),
                    g.image.load('Run (7).png'),g.image.load('Run (8).png')]

run_img_left_p1 = [g.transform.flip(run_img_right_p1[0],1,0),g.transform.flip(run_img_right_p1[1],1,0),
                   g.transform.flip(run_img_right_p1[2],1,0),g.transform.flip(run_img_right_p1[3],1,0),
                   g.transform.flip(run_img_right_p1[4],1,0),g.transform.flip(run_img_right_p1[5],1,0),
                   g.transform.flip(run_img_right_p1[6],1,0),g.transform.flip(run_img_right_p1[7],1,0)]

idle_img_p1 = g.image.load('idle.png')
bullet_img = g.image.load('bullet.png')

#player2
run_img_right_p2 = [g.image.load('Run__000.png'),g.image.load('Run__001.png'),g.image.load('Run__002.png'),
                    g.image.load('Run__003.png'),g.image.load('Run__004.png'),g.image.load('Run__005.png'),
                    g.image.load('Run__006.png'),g.image.load('Run__007.png'),g.image.load('Run__008.png'),
                    g.image.load('Run__009.png')]

run_img_left_p2 = [g.transform.flip(run_img_right_p2[0],1,0),g.transform.flip(run_img_right_p2[1],1,0),
                   g.transform.flip(run_img_right_p2[2],1,0),g.transform.flip(run_img_right_p2[3],1,0),
                   g.transform.flip(run_img_right_p2[4],1,0),g.transform.flip(run_img_right_p2[5],1,0),
                   g.transform.flip(run_img_right_p2[6],1,0),g.transform.flip(run_img_right_p2[7],1,0),
                   g.transform.flip(run_img_right_p2[8],1,0),g.transform.flip(run_img_right_p2[9],1,0)]

idle_img_p2 = g.image.load('idle__001.png')
blade_img = g.image.load('blade.png')

#clock
clock = g.time.Clock()


# main characters
class character:
    def __init__(self,x, width, height,player):
        self.player = player
        self.width = width
        self.height = height
        self.x = x
        self.y = win_height-height+ 5
        self.speed =10
        self.on_ground = False
        self.jump_time_const = 8.5
        self.jump_time = self.jump_time_const
        self.m_left = False
        self.m_right =False
        self.step_count = 0
        self.is_standing = True
        self.hit_box = (self.x+20,self.y,28,60)

        # width_main = 102
        # height_main = 100
        # x_main = 50
        # y_main = win_height-height_main+ 5
        # speed_main = 5
        # on_ground_main = True
        #
        # jump_time_main_const = 8  # set the height and time for the jump
        # jump_time_main = jump_time_main_const
        #
        # m_left_main = True
        # m_right_main = False
        # step_count_main = 0


    def draw(self,win):
        if self.player == 1:
            if self.step_count + 1 > 24:
                self.step_count = 0

        elif self.player == 2:
            if self.step_count + 1 > 30:
                self.step_count = 0

        if self.is_standing == False:
            if self.m_left == True:
                if self.player == 1:
                    win.blit(run_img_left_p1[self.step_count // 3], (self.x, self.y))
                elif self.player == 2:
                    win.blit(run_img_left_p2[self.step_count // 3], (self.x, self.y))

                self.step_count += 1

            elif self.m_right == True:
                if self.player == 1:
                    win.blit(run_img_right_p1[self.step_count // 3], (self.x, self.y))
                elif self.player == 2:
                    win.blit(run_img_right_p2[self.step_count // 3], (self.x, self.y))

                self.step_count += 1

        else:
            if self.m_right == False and self.m_left == False:
                if self.player == 1:
                    win.blit(idle_img_p1, (self.x, self.y))
                elif self.player == 2:
                    win.blit(g.transform.flip(idle_img_p2, 1, 0), (self.x, self.y))

            elif self.m_left == True:
                if self.player == 1:
                    win.blit(g.transform.flip(idle_img_p1, 1, 0), (self.x, self.y))

                if self.player == 2:
                    win.blit(g.transform.flip(idle_img_p2, 1, 0), (self.x, self.y))

            else:
                if self.player == 1:
                    win.blit(idle_img_p1, (self.x, self.y))
                if self.player == 2:
                    win.blit(idle_img_p2, (self.x, self.y))
        if self.player == 2:
            self.hit_box = (self.x+6, self.y, 40, 100)
        else:
            self.hit_box = (self.x + 28, self.y+10, 40, 85)
        g.draw.rect(win,(255,0,0),self.hit_box,2)


class range_weapons:
    def __init__(self,x,y,side,player):
        self.x= x
        self.y = y
        self.side = side
        self.speed = 20*side
        self.player = player


    def draw(self,win):
        if self.player == 1:
            if self.side == 1:
                win.blit(bullet_img,(self.x,self.y))
            else:
                win.blit(g.transform.flip(bullet_img,1,0), (self.x, self.y))
        elif self.player == 2:
            if self.side == 1:
                win.blit(blade_img,(self.x,self.y))
            else:
                win.blit(g.transform.flip(blade_img,1,0), (self.x, self.y))

def refresh_win():
    win.blit(bg, (0,-120))
    p1.draw(win)
    p2.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    for blade in blades:
        blade.draw(win)

    g.display.update()

p1 = character(50, 102, 100, 1)
p2 = character(win_width - 50 - 53, 102, 100, 2)
bullets = []    # list of all bullet objects (elements are instance of range weapons): Player 1
blades = []     # list pf all blade objects (elements are instance of range weapons): Player 2

flag = True
while flag:
    clock.tick(27)
    for change in g.event.get():
        if change.type == g.QUIT:
            flag = False

    for bullet in bullets:
        if bullet.x < win_width and bullet.x > 0:
            bullet.x += bullet.speed
        else:
            bullets.pop(bullets.index(bullet))

    for blade in blades:
        if blade.x < win_width and blade.x > 0:
            blade.x += blade.speed
        else:
            blades.pop(blades.index(blade))

    key = g.key.get_pressed()

    if key[g.K_TAB]:
        if p2.m_left == True or (p2.m_left == False and p2.m_right == False):
            side = -1
        else:
            side = 1

        if len(blades) < 5:
            blades.append(range_weapons(round(p2.x + p2.width // 2), round(p2.y + p2.height // 2), side,2))
    if key[g.K_SPACE]:
        if p1.m_right == True or (p2.m_left == False and p2.m_right == False) :
            side = 1
        else:
            side = -1
        if len(bullets) < 5:
            bullets.append(range_weapons(round(p1.x+p1.width//2), round(p1.y +p1.height//2), side, 1))


    if key[g.K_LEFT] and p1.x > p1.speed:
        p1.x = p1.x - p1.speed
        p1.m_left = True
        p1.m_right = False
        p1.is_standing = False

    elif key[g.K_RIGHT] and p1.x <win_width-p1.speed - p1.width:
        p1.x = p1.x + p1.speed
        p1.m_left = False
        p1.m_right = True
        p1.is_standing = False

    else:
        p1.is_standing =True
        p1.step_count = 0

    if key[g.K_UP] and p1.on_ground:
        p1.on_ground = False
        p1.m_right = False
        p1.m_left = False
        p1.step_count = 0

    if p1.on_ground ==False:
        if p1.jump_time>= -1*p1.jump_time_const:
            const = 0.5
            if p1.jump_time < 0:
                const = -0.5
            p1.y -= (p1.jump_time ** 2) * const
            p1.jump_time -= 1
        else:
            p1.jump_time = p1.jump_time_const
            p1.on_ground = True


    if key[g.K_a] and p2.x > p2.speed:
        p2.x = p2.x - p2.speed
        p2.m_left = True
        p2.m_right = False
        p2.is_standing = False

    elif key[g.K_d] and p2.x < win_width - p2.speed - p2.width:
        p2.x = p2.x + p2.speed
        p2.m_left = False
        p2.m_right = True
        p2.is_standing = False

    else:
        p2.is_standing = True
        p2.step_count = 0

    if key[g.K_w] and p2.on_ground:
        p2.on_ground = False
        p2.m_right = False
        p2.m_left = False
        p2.step_count = 0

    if p2.on_ground == False:
        if p2.jump_time >= -1 * p2.jump_time_const:
            const = 0.5
            if p2.jump_time < 0:
                const = -0.5
            p2.y -= (p2.jump_time ** 2) * const
            p2.jump_time -= 1
        else:
            p2.jump_time = p2.jump_time_const
            p2.on_ground = True

    refresh_win()

g.quit()
print("Done")

# robo.y = robo.y + force_main - gravity
# if key[g.K_DOWN] and robo.y< win_height -robo.speed-robo.height:
# robo.y = y_main + robo.speed