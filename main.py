import pygame
import title_screen
import menu_screen
import button_screen

DISPLAY = pygame.display.set_mode((1280,720))

title_screen.draw(DISPLAY)
while True:
    choice = menu_screen.draw(DISPLAY)
    if choice == "button":
        button_screen.draw(DISPLAY)

