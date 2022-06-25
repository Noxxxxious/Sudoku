import pygame


class Field:
    def __init__(self, digit, x, y, size):
        self.__x = x * size
        self.__y = y * size
        self.__size = size
        self.__size = size
        self.__digit = digit
        self.__isFinal = False
        self.font = pygame.font.SysFont("Arial", 32)

    def draw(self, surface, color):
        rect = pygame.rect.Rect(self.__x, self.__y, self.__size, self.__size)
        pygame.draw.rect(surface, color, rect)
        if self.__digit is None:
            return
        text = self.font.render(str(self.__digit), False, (150, 150, 150))
        text_rect = text.get_rect(center=(rect.x + self.__size / 2, rect.y + self.__size / 2))
        surface.blit(text, text_rect)

    def set_digit(self, digit):
        self.__digit = digit

    def get_digit(self):
        return self.__digit

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_size(self):
        return self.__size
