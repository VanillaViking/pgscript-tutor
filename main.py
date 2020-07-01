import pygame
import title_screen
import menu_screen
import button_screen
import text_input_screen
import slider_screen
import draggable_screen
import scrolling_bg_screen
import parallax_bg_screen
import text_screen
import grid_screen
import scroll_screen

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
    elif choice == "p_bg":
        parallax_bg_screen.draw(DISPLAY)
    elif choice == "text":
        text_screen.draw(DISPLAY)
    elif choice == "scroll":
        scroll_screen.draw(DISPLAY) 
    elif choice == "grid":
        grid_screen.draw(DISPLAY)



