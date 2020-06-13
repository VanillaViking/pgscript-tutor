import pygame
from pgscript import draw_grid
from pgscript import scrolling_screen
from pgscript import bg
from pgscript import text
from pgscript import button

def draw(DISPLAY):
    screen = scrolling_screen.scrolling_screen(DISPLAY, 2, "r", 20, 15, (230,230,230))
    grid = draw_grid.draw_grid(screen.surface, 5, 16)
    
    #surfaces to draw scrolling bgs on. this way, the background will only be drawn where these surfaces exist. (sides of the screen)
    bg_surf_l = pygame.Surface((grid.get_column(1), screen.surface.get_height())) 
    bg_surf_r = pygame.Surface((grid.get_column(1), screen.surface.get_height())) 

    background_l = bg.scrolling_bg(bg_surf_l, (82,9,124), ["tringle.png"], 60)
    background_r = bg.scrolling_bg(bg_surf_r, (82,9,124), ["tringle.png"], 60)

    background_r.anim_start()
    background_l.anim_start()

    heading = text.text(screen.surface, pygame.font.SysFont('arial', 40), (255,255,255))
    heading.message("Select an Object", (grid.get_column(2.5), grid.get_row(1)))

    #BUTTONS

    button_btn = button.button(screen.surface, [200,200,200,100],[255,130,245,200], grid.get_column(1.5)- 75, grid.get_row(3.5) - 75, 150,150, "Button", anim=True, font_size=24) 
    text_input_btn = button.button(screen.surface, [200,200,200,100],[255,130,245,200], grid.get_column(2.5)- 75, grid.get_row(3.5) - 75, 150,150, "Text Input", anim=True, font_size=24) 
    slider_btn = button.button(screen.surface, [200,200,200,100],[255,130,245,200], grid.get_column(3.5)- 75, grid.get_row(3.5) - 75, 150,150, "Slider", anim=True, font_size=24) 

    draggable_btn = button.button(screen.surface, [200,200,200,100],[255,130,245,200], grid.get_column(1.5)- 75, grid.get_row(6) - 75, 150,150, "Draggable Surface", anim=True, wrapping=9, font_size=24) 
    text_btn = button.button(screen.surface, [200,200,200,100],[255,130,245,200], grid.get_column(2.5)- 75, grid.get_row(6) - 75, 150,150, "Text", anim=True, font_size=24) 
    bg_btn = button.button(screen.surface, [200,200,200,100],[255,130,245,200], grid.get_column(3.5)- 75, grid.get_row(6) - 75, 150,150, "Backgrounds", anim=True, font_size=24)

    anim_btn = button.button(screen.surface, [200,200,200,100],[255,130,245,200], grid.get_column(1.5)- 75, grid.get_row(8.5) - 75, 150,150, "Animations", anim=True, font_size=24) 
    grid_btn = button.button(screen.surface, [200,200,200,100],[255,130,245,200], grid.get_column(2.5)- 75, grid.get_row(8.5) - 75, 150,150, "Grid", anim=True, font_size=24) 
    scroll_btn = button.button(screen.surface, [200,200,200,100],[255,130,245,200], grid.get_column(3.5)- 75, grid.get_row(8.5) - 75, 150,150, "Scrolling Screen", anim=True, font_size=24, wrapping=10) 

    screen.add_objects([heading, button_btn, text_input_btn, slider_btn, draggable_btn, text_btn, bg_btn, anim_btn, grid_btn, scroll_btn])

    while True:
        pygame.display.update()
        screen.surface.fill((82,9,124))
        
        background_l.draw()
        background_r.draw()
        
        screen.surface.blit(bg_surf_l, (0,0))
        screen.surface.blit(bg_surf_r, (DISPLAY.get_width() - bg_surf_r.get_width(),0))

        screen.draw()

        for event in pygame.event.get():
            screen.update(event)

