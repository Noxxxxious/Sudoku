import pygame
from Sudoku import Sudoku
from GameWindow import GameWindow

if __name__ == "__main__":
    pygame.init()
    window = GameWindow()
    sudoku = Sudoku(window)
    sudoku.board_generator()
    while not sudoku.is_over():
        sudoku.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                sudoku.click(pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():
                    sudoku.write(event.unicode)
                if event.key == pygame.K_BACKSPACE:
                    sudoku.remove()
