import pygame
from constants import WIDTH, HEIGHT


class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        # self.width = 150
        self.width = WIDTH // 5
        # self.height = 100
        self.height = HEIGHT // 10

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        # font = pygame.font.SysFont("comicsans", 40)
        font = pygame.font.SysFont("comicsans", 20)
        text = font.render(self.text, True, (255, 255, 255))
        window.blit(
            text,
            (
                self.x + round(self.width/2) - round(text.get_width()/2),
                self.y + round(self.height/2) - round(text.get_height()/2)
            )
        )

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False
