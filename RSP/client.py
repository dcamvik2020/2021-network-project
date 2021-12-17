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
        font_size = min(WIDTH // 20, HEIGHT // 20)
        font = pygame.font.SysFont("comicsans", font_size)
        text = font.render("Click to Play!", True, THECOLORS['green'])
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
