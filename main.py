###################################
# 2 player game project           #
# By: Vrajang Parikh              #
# Last updated Date: 3 July, 2019 #
###################################



import pygame as g
import intro
import player

g.init()

#initialize console & font
win_width = 1200
win_height = 600
win = g.display.set_mode((win_width,win_height))
g.display.set_caption("Fighter")
font = g.font.SysFont('Helvetica',30,True)

#background image
bg = g.image.load('bg.gif')

#sounds
bullet_sound = g.mixer.Sound('bullet.wav')
bullet_sound.set_volume(0.1)
blade_sound= g.mixer.Sound('blade.wav')
blade_sound.set_volume(0.13)
bg_music = g.mixer.music.load("bg.mp3")
g.mixer.music.set_volume(0.2)
g.mixer.music.play(-1)

#clock
clock = g.time.Clock()

game_type = intro.game_intro(win,clock)


# players
#x pos,width,height,player #, win_width,win_height,game_type
p1 = player.character(50, 102, 100, 1,win_width,win_height,game_type)
p2 = player.character(win_width - 50 - 53, 102, 100, 2,win_width,win_height,game_type)

bullets = []    # list of all bullet objects (elements are instance of range weapons): Player 1
blades = []     # list pf all blade objects (elements are instance of range weapons): Player 2

#update win and draw objects
def refresh_win(game_type):
    win.blit(bg, (0,-120))
    p1.draw(win,game_type)
    p2.draw(win,game_type)
    if game_type == 1:
        text1 = font.render('Player 1: {}'.format(p1.points), 1,(255,69,0))
        text2 = font.render('Player 2: {}'.format(p2.points), 1, (255,69,0))
        text3 = font.render('Press Esc to quit',1,(66, 197, 245))
        win.blit(text1,(50 ,10))
        win.blit(text2,(1000,10))
        win.blit(text3, (490 ,30))
        for bullet in bullets:
            bullet.draw(win)
        for blade in blades:
            blade.draw(win)

    if p1.is_dead == False and game_type == 2:
        for bullet in bullets:
            bullet.draw(win)
    if p2.is_dead == False and  game_type == 2:
        for blade in blades:
            blade.draw(win)

    g.display.update()

def game_loop(game_type):

    cooldown_bullets = 0
    cooldown_blades = 0
    is_esc = False
    flag = True
    while flag:
        clock.tick(27)
        for change in g.event.get():
            if change.type == g.QUIT:
                g.quit()
                flag = False

        key = g.key.get_pressed()
        is_esc = key[g.K_ESCAPE]
        if (p1.is_dead == False and game_type == 2) or (game_type == 1 and not (key[g.K_ESCAPE])):
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
                            if game_type == 2:
                                p2.hit()
                            else:
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
                    bullets.append(player.range_weapons(round(p1.x + p1.width // 2), round(p1.y + p1.height // 2), side, 1, 25, 20))
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

        if p2.is_dead == False and game_type == 2 or (game_type == 1 and not(key[g.K_ESCAPE])):
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
                            if game_type ==2:
                                p1.hit()
                            else:
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
                        blades.append(player.range_weapons(round(p2.x - p2.width // 2), round(p2.y + p2.height // 2), side,2,80,16))
                    else:
                        blades.append(player.range_weapons(round(p2.x + p2.width // 2), round(p2.y + p2.height // 2), side, 2, 80, 16))

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

        if is_esc == True or p1.is_dead or p2.is_dead:
            flag = False
        #drawing objects
        refresh_win(game_type)

def announce_winner():
    winner = 0
    if game_type == 1:
        if p1.points > p2.points:
            winner = 1
        elif p1.points < p2.points:
            winner = 2
    else:
        if p1.is_dead == True:
            winner = 2
        else:
            winner = 1

    flag = True
    option = 0
    while flag:
        clock.tick(27)
        win.blit(bg, (0, -120))

        pos = g.mouse.get_pos()

        if winner == 1:
            win.blit(g.image.load('p1_wins.png'),(0,0))
        elif winner == 2:
            win.blit(g.image.load('p2_wins.png'), (0,0))
        else:
            win.blit(g.image.load('tie_game.png'), (0,0))

        if option == 1:
            win.blit(g.image.load('credits.png'), (0, 0))
            if change.type == g.MOUSEBUTTONDOWN:
                if 960 <= pos[0] <= 1166 and 510 <= pos[1] <= 590:
                    option = 0
            # Play again- g.draw.rect(win, (0, 0, 0), (448, 308, 333, 80), 0)
        # Credits- g.draw.rect(win, (0, 0, 0), (495, 398, 233, 80), 0)
        # Quit- g.draw.rect(win, (0, 0, 0), (517, 495, 195, 80), 0)

        for change in g.event.get():
            if change.type == g.QUIT:
                g.quit()
                flag = False
            if change.type == g.MOUSEBUTTONDOWN:
                if 448 <= pos[0] <= 781 and 308 <= pos[1] <= 388:
                    flag = False
                    return 0
                elif 495 <= pos[0] <= 728 and 398 <= pos[1] <= 478:
                    option = 1

                elif 517 <= pos[0] <= 712 and 495 <= pos[1] <= 575:
                    flag = False
                    return 1
                    g.quit()
        g.display.update()



game_loop(game_type)
choice = announce_winner()

while choice == 0:
    game_type = intro.game_intro(win, clock)

    # players
    # x pos,width,height,player #, win_width,win_height,game_type
    p1 = player.character(50, 102, 100, 1, win_width, win_height, game_type)
    p2 = player.character(win_width - 50 - 53, 102, 100, 2, win_width, win_height, game_type)
    bullets = []  # list of all bullet objects (elements are instance of range weapons): Player 1
    blades = []  # list pf all blade objects (elements are instance of range weapons): Player 2
    game_loop(game_type)
    choice = announce_winner()

g.quit()



