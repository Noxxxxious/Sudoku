import pygame
pygame.init()


class GameWindow:
    def __init__(self):
        self.size = 594
        self.icon = pygame.image.load("images/icon.png")
        self.font = pygame.font.SysFont("Arial", 32)
        self.surface = pygame.display.set_mode((self.size, self.size))

        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("Sudoku")

