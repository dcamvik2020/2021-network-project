import pygame
from network import Network
import pickle

from button import Button
from pygame.colordict import THECOLORS
from redrawing_window import redraw_window, btns
from constants import WIDTH, HEIGHT

pygame.font.init()


win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")

#
# def redraw_window(window, width, height, game, p):
#     window.fill((128, 128, 128))
#
#     if not(game.connected()):
#         font = pygame.font.SysFont("comicsans", 80)
#         text = font.render("Waiting for Player...", True, (255, 0, 0), True)
#         window.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
#     else:
#         font = pygame.font.SysFont("comicsans", 60)
#         text = font.render("Your Move", True, (0, 255, 255))
#         window.blit(text, (80, 200))
#
#         text = font.render("Opponents", True, (0, 255, 255))
#         window.blit(text, (380, 200))
#
#         move1 = game.get_player_move(0)
#         move2 = game.get_player_move(1)
#         if game.both_went():
#             text1 = font.render(move1, True, (0, 0, 0))
#             text2 = font.render(move2, True, (0, 0, 0))
#         else:
#             if game.p1Went and p == 0:
#                 text1 = font.render(move1, True, (0, 0, 0))
#             elif game.p1Went:
#                 text1 = font.render("Locked In", True, (0, 0, 0))
#             else:
#                 text1 = font.render("Waiting...", True, (0, 0, 0))
#
#             if game.p2Went and p == 1:
#                 text2 = font.render(move2, True, (0, 0, 0))
#             elif game.p2Went:
#                 text2 = font.render("Locked In", True, (0, 0, 0))
#             else:
#                 text2 = font.render("Waiting...", True, (0, 0, 0))
#
#         if p == 1:
#             window.blit(text2, (100, 350))
#             window.blit(text1, (400, 350))
#         else:
#             window.blit(text1, (100, 350))
#             window.blit(text2, (400, 350))
#
#         for btn in btns:
#             btn.draw(window)
#
#     pygame.display.update()
#
#
# btns = [
#     Button("Rock", 50, 500, (0, 0, 0)),
#     Button("Scissors", 250, 500, (255, 0, 0)),
#     Button("Paper", 450, 500, (0, 255, 0))
# ]


def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.get_p())
    print("You are player", player)

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except Exception as e:
            print(e)
            # run = False    # not needed since break will do exit
            print("Couldn't get game")
            break

        if game.both_went():
            redraw_window(win, WIDTH, HEIGHT, game, player)
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except Exception as e:
                print(e)
                # run = False
                print("Couldn't get game")
                break

            font = pygame.font.SysFont("comicsans", 90)
            if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
                text = font.render("You Won!", True, (255, 0, 0))
            elif game.winner() == -1:
                text = font.render("Tie Game!", True, (255, 0, 0))
            else:
                text = font.render("You Lost...", True, (255, 0, 0))

            win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game.connected():
                        if player == 0:
                            if not game.p1Went:
                                n.send(btn.text)
                        else:
                            if not game.p2Went:
                                n.send(btn.text)

        redraw_window(win, WIDTH, HEIGHT, game, player)


def menu():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill((128, 128, 128))
        # font = pygame.font.SysFont("comicsans", 60)
        font_size = min(WIDTH // 20, HEIGHT // 20)
        font = pygame.font.SysFont("comicsans", font_size)
        text = font.render("Click to Play!", True, THECOLORS['green'])
        # win.blit(text, (100, 200))
        win.blit(text, ((WIDTH - text.get_width()) // 2, (HEIGHT - text.get_height()) // 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()


while True:
    menu()
