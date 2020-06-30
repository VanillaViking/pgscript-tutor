import pygame
import title_screen
import menu_screen
import button_screen
import text_input_screen
import slider_screen
import draggable_screen
import scrolling_bg_screen

DISPLAY = pygame.display.set_mode((1280,720))

title_screen.draw(DISPLAY)
while True:
    choice = menu_screen.draw(DISPLAY)
    if choice == "button":
        button_screen.draw(DISPLAY)
    elif choice == "text_input":
        text_input_screen.draw(DISPLAY) 
    elif choice == "slider":
        slider_screen.draw(DISPLAY) 
    elif choice == "drag":
        draggable_screen.draw(DISPLAY)
    elif choice == "s_bg":
        scrolling_bg_screen.draw(DISPLAY)


