import pygame
import title_screen
import menu_screen

DISPLAY = pygame.display.set_mode((1280,720))

title_screen.draw(DISPLAY)
menu_screen.draw(DISPLAY)

