from button import Button
import pygame
from pygame.colordict import THECOLORS

btns = [
    Button("Rock", 50, 500, (200, 0, 0)),
    Button("Scissors", 250, 500, (0, 200, 0)),
    Button("Paper", 450, 500, (0, 0, 200))
]


def redraw_window(window, width, height, game, p):
    window.fill((128, 128, 128))

    font_size = min(width // 20, height // 20)

    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", font_size)
        # text = font.render("Waiting for Player...", True, (255, 0, 0), True)
        # text = font.render("Waiting for Player...", True, THECOLORS['yellow'], True)
        text = font.render("Waiting for Player...", True, THECOLORS['yellow'])
        window.fill((128, 128, 128))
        window.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
    else:
        # first line : 'your move' ... 'waiting'
        # font = pygame.font.SysFont("comicsans", 60)
        font = pygame.font.SysFont("comicsans", font_size)
        text = font.render("Your Move", True, (0, 255, 255))
        # text_pos = (80, 200)
        text_pos = ((width // 2 - text.get_width()) // 2, (height - text.get_height()) // 10)
        window.blit(text, text_pos)

        # second line : 'your move' ... 'waiting'
        text = font.render("Opponents", True, (0, 255, 255))
        # text_pos = (380, 200)
        text_pos = (width // 2 + (width // 2 - text.get_width()) // 2, (height - text.get_height()) // 10)
        window.blit(text, text_pos)

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

        text_1_pos = ((width // 2 - text1.get_width()) // 2, (height - text1.get_height()) // 10 * 2)
        text_2_pos = (width // 2 + (width // 2 - text2.get_width()) // 2, (height - text2.get_height()) // 10 * 2)
        if p == 1:
            # window.blit(text2, (100, 350))
            window.blit(text2, text_1_pos)
            # window.blit(text1, (400, 350))
            window.blit(text1, text_2_pos)
        else:
            # window.blit(text1, (100, 350))
            window.blit(text1, text_1_pos)
            # window.blit(text2, (400, 350))
            window.blit(text2, text_2_pos)

        for btn in btns:
            btn.draw(window)

    pygame.display.update()
