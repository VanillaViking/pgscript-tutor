import pygame
from pgscript import bg
from pgscript import button
from pgscript import text
from pgscript import draw_grid

def draw(DISPLAY):
    grid = draw_grid.draw_grid(DISPLAY, 5, 4)

    bg_surf_l = pygame.Surface((grid.get_column(1), DISPLAY.get_height())) 
    bg_surf_r = pygame.Surface((grid.get_column(1), DISPLAY.get_height())) 

    background_l = bg.scrolling_bg(bg_surf_l, (82,9,124), ["tringle.png"], 30)
    background_r = bg.scrolling_bg(bg_surf_r, (82,9,124), ["tringle.png"], 30)

    background_r.anim_start()
    background_l.anim_start()

    heading = text.text(DISPLAY, pygame.font.SysFont('arial', 40), (255,255,255))
    heading.message("PGSCRIPT TUTOR", (grid.get_column(2.5), grid.get_row(1)), center=True)

    cont_button = button.button(DISPLAY, [200,200,200,100], [200,200,200,200], grid.get_column(2.5) - 80, (grid.get_row(3)) - 37, 160,75, "Continue", anim=True)

    while not cont_button.get_state():
        pygame.display.update()
        DISPLAY.fill((82,9,124))
        heading.draw()
        cont_button.draw()

        background_l.draw()
        background_r.draw()

        DISPLAY.blit(bg_surf_l, (0,0))
        DISPLAY.blit(bg_surf_r, (DISPLAY.get_width() - bg_surf_r.get_width(),0))


        for event in pygame.event.get():
            cont_button.update(event)
