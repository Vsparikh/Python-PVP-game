import pygame as g
g.init()
#welcome screen
#returns game mode
def game_intro(win,clock):
    option = 0
    intro_img = g.image.load('intro.png')
    credits_img = g.image.load('credits.png')
    how_to_play = g.image.load('how_to_play.png')
    game_mode = g.image.load('game_mode.png')
    win.blit(intro_img, (0, 0))


    #button position
    #Go- g.draw.rect(win,(0,0,0),(512,207,206,80),0)
    #How to Play- g.draw.rect(win, (0, 0, 0), (448, 308, 333, 80), 0)
    #Credits- g.draw.rect(win, (0, 0, 0), (495, 398, 233, 80), 0)
    #Quit- g.draw.rect(win, (0, 0, 0), (517, 495, 195, 80), 0)

    flag = True
    while flag:
        clock.tick(30)
        for change in g.event.get():
            if change.type == g.QUIT:
                flag = False
                g.quit()
        pos = g.mouse.get_pos()
        if option == 0:
            win.blit(intro_img, (0, 0))
            if change.type == g.MOUSEBUTTONDOWN:
                if 512 <= pos[0] <= 718 and 207 <= pos[1] <= 287:
                    option = 1
                elif 448 <= pos[0] <= 781 and 308 <= pos[1] <= 388:
                    option = 2
                elif 495 <= pos[0] <= 728 and 398 <= pos[1] <= 478:
                    option = 3
                elif 517 <= pos[0] <= 712 and 495 <= pos[1] <= 575:
                    flag = False
                    g.quit()

        elif option == 2:
            win.blit(how_to_play,(0,0))
            #g.draw.rect(win, (0, 0, 0), (960, 510, 206, 80), 0)
            if change.type == g.MOUSEBUTTONDOWN:
                if 960 <= pos[0] <= 1166 and 510 <= pos[1] <= 590:
                    option = 0

        elif option == 3:
            win.blit(credits_img,(0,0))
            if change.type == g.MOUSEBUTTONDOWN:
                if 960 <= pos[0] <= 1166 and 510 <= pos[1] <= 590:
                    option = 0

        elif option == 1:
            win.blit(game_mode,(0,0))
            if change.type == g.MOUSEBUTTONDOWN:
                if 448 <= pos[0] <= 781 and 308 <= pos[1] <= 388:
                    flag = False
                    return 1
                elif 495 <= pos[0] <= 728 and 398 <= pos[1] <= 478:
                    flag = False
                    return 2
                elif 517 <= pos[0] <= 712 and 495 <= pos[1] <= 575:
                    game_intro(win,clock)

        g.display.update()

    g.quit()