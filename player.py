import pygame as g

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


# main characters
class character:
    def __init__(self,x, width, height,player,win_width,win_height,game_type):
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
        self.hit_box = (self.x+20,self.y,28,60)  #(x,y,width,height)- rectangle
        self.health_const = 200
        self.healh = 200
        self.points = 0
        self.is_dead = False
        self.game_type = game_type


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

    def draw(self,win,game_type):
        if self.is_dead == False:
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

            if self.game_type == 2:
                if self.player == 1:
                    g.draw.rect(win, (50,205,50), (self.x, self.y-20, 100 - (100 - (self.healh//(self.health_const/100))), 10))
                    g.draw.rect(win, (50, 205, 50), (self.x, self.y - 20, 100, 10),2)
                else:
                    g.draw.rect(win, (50,205,50), (self.x - 22, self.y - 20,100- (100 - (self.healh//(self.health_const/100))), 10))
                    g.draw.rect(win, (50, 205, 50), (self.x - 22, self.y - 20, 100, 10),2)

                # g.draw.rect(win,(255,0,0),self.hit_box,2)


    def hit(self):
        if self.healh >=5:
            self.healh -= 5
        else:
            self.is_dead = True

#weapons for players
class range_weapons:
    def __init__(self,x,y,side,player,width,height):
        self.x= x
        self.y = y
        self.side = side
        self.speed = 20*side
        self.player = player
        self.width = width
        self.height = height

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


# robo.y = robo.y + force_main - gravity
# if key[g.K_DOWN] and robo.y< win_height -robo.speed-robo.height:
# robo.y = y_main + robo.speed