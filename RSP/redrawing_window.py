from button import Button
import pygame


btns = [
    Button("Rock", 50, 500, (0, 0, 0)),
    Button("Scissors", 250, 500, (255, 0, 0)),
    Button("Paper", 450, 500, (0, 255, 0))
]


def redraw_window(window, width, height, game, p):
    window.fill((128, 128, 128))

    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", True, (255, 0, 0), True)
        window.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Your Move", True, (0, 255, 255))
        window.blit(text, (80, 200))

        text = font.render("Opponents", True, (0, 255, 255))
        window.blit(text, (380, 200))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.both_went():
            text1 = font.render(move1, True, (0, 0, 0))
            text2 = font.render(move2, True, (0, 0, 0))
        else:
            if game.p1Went and p == 0:
                text1 = font.render(move1, True, (0, 0, 0))
            elif game.p1Went:
                text1 = font.render("Locked In", True, (0, 0, 0))
            else:
                text1 = font.render("Waiting...", True, (0, 0, 0))

            if game.p2Went and p == 1:
                text2 = font.render(move2, True, (0, 0, 0))
            elif game.p2Went:
                text2 = font.render("Locked In", True, (0, 0, 0))
            else:
                text2 = font.render("Waiting...", True, (0, 0, 0))

        if p == 1:
            window.blit(text2, (100, 350))
            window.blit(text1, (400, 350))
        else:
            window.blit(text1, (100, 350))
            window.blit(text2, (400, 350))

        for btn in btns:
            btn.draw(window)

    pygame.display.update()
