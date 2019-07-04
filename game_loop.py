import pygame as g
import player
class play_game:
    def __init__(self,win,win_width, win_height):
        self.win = win
        self.win_width = win_width
        self.win_height = win_height


    # players
    #x pos,width,height,player #, win_width,win_height
    player.p1 = player.character(50, 102, 100, 1,self.win_width,self.win_height)
    player.p2 = player.character(self.win_width - 50 - 53, 102, 100, 2,self.win_width,self.win_height)

    bullets = []    # list of all bullet objects (elements are instance of range weapons): Player 1
    blades = []     # list pf all blade objects (elements are instance of range weapons): Player 2
    cooldown_bullets = 0
    cooldown_blades = 0


#update win and draw objects
def refresh_win(win,font,bg):
    win.blit(bg, (0,-120))
    text1 = font.render('Player 1: {}'.format(p1.points), 1,(255,69,0))
    text2 = font.render('Player 2: {}'.format(p2.points), 1, (255,69,0))
    win.blit(text1,(50 ,10))
    win.blit(text2,(1000,10))
    p1.draw(win)
    p2.draw(win)
    if p1.is_dead == False:
        for bullet in bullets:
            bullet.draw(win)
    if p2.is_dead == False:
        for blade in blades:
            blade.draw(win)

    g.display.update()

flag = True

def play_game():
    while flag:
        clock.tick(27)
        for change in g.event.get():
            if change.type == g.QUIT:
                g.quit()
                flag = False

        key = g.key.get_pressed()

        if p1.is_dead == False:
            #adding cooldown period to avoid spamming
            if cooldown_bullets >= 3:
                cooldown_bullets = 0
            elif cooldown_bullets >= 0:
                cooldown_bullets += 1

            # set position of  bullets
            for bullet in bullets:
                if bullet.y >= p2.y and bullet.y + bullet.height <= p2.y + p2.height:
                    if bullet.x + bullet.width >= p2.x and bullet.x <= p2.x + p2.width:
                        if p2.is_dead == False:
                            p2.hit()
                            p1.points += 1
                        bullets.pop(bullets.index(bullet))

                if bullet.x < win_width and bullet.x > 0:
                    bullet.x += bullet.speed
                else:
                    bullets.pop(bullets.index(bullet))

            #shooting bullets
            if key[g.K_SPACE] and cooldown_bullets == 0:
                if p1.m_right == True or (p1.m_left == False and p1.m_right == False):
                    side = 1
                else:
                    side = -1
                if len(bullets) < 5:
                    bullet_sound.play()
                    bullets.append(range_weapons(round(p1.x + p1.width // 2), round(p1.y + p1.height // 2), side, 1, 25, 20))
                    cooldown_bullets = 1

            # moving characters
            if key[g.K_LEFT] and p1.x > p1.speed:
                p1.x = p1.x - p1.speed
                p1.m_left = True
                p1.m_right = False
                p1.is_standing = False

            elif key[g.K_RIGHT] and p1.x < win_width - p1.speed - p1.width:
                p1.x = p1.x + p1.speed
                p1.m_left = False
                p1.m_right = True
                p1.is_standing = False

            else:
                p1.is_standing = True
                p1.step_count = 0

            if key[g.K_UP] and p1.on_ground:
                p1.on_ground = False
                # p1.m_right = False
                # p1.m_left = False
                p1.step_count = 0

            if p1.on_ground == False:
                if p1.jump_time >= -1 * p1.jump_time_const:
                    const = 0.5
                    if p1.jump_time < 0:
                        const = -0.5
                    p1.y -= (p1.jump_time ** 2) * const
                    p1.jump_time -= 1
                else:
                    p1.jump_time = p1.jump_time_const
                    p1.on_ground = True

        if p2.is_dead == False:
            #player 2
            # adding cooldown period to avoid spamming
            if cooldown_blades >= 3:
                cooldown_blades = 0
            elif cooldown_blades >= 0:
                cooldown_blades += 1

            # set position of  bullets
            for blade in blades:
                if blade.y >= p1.y and blade.y + blade.height <= p1.y + p1.height:
                    if blade.x + blade.width >=p1.x and blade.x <=p1.x+ p1.width:
                        if p1.is_dead == False:
                            p1.hit()
                            p2.points += 1
                        blades.pop(blades.index(blade))

                if blade.x < win_width and blade.x > 0:
                    blade.x += blade.speed
                else:
                    blades.pop(blades.index(blade))

            #shooting blades
            if key[g.K_TAB] and cooldown_blades == 0:
                if p2.m_left == True or (p2.m_left == False and p2.m_right == False):
                    side = -1
                else:
                    side = 1

                if len(blades) < 5:
                    blade_sound.play()
                    if side == -1:
                        blades.append(range_weapons(round(p2.x - p2.width // 2), round(p2.y + p2.height // 2), side,2,80,16))
                    else:
                        blades.append(range_weapons(round(p2.x + p2.width // 2), round(p2.y + p2.height // 2), side, 2, 80, 16))

                    cooldown_blades = 1

            # moving characters
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
                # p2.m_right = False
                # p2.m_left = False
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


        #drawing objects
        refresh_win()
