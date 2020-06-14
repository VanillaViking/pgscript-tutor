import pygame
from pgscript import draw_grid
from pgscript import scrolling_screen
from pgscript import text
from pgscript import bg
from pgscript import button

def draw(DISPLAY):
    grid = draw_grid.draw_grid(DISPLAY, 2, 8)

    doc_surf = pygame.Surface((DISPLAY.get_width(), DISPLAY.get_height()))

    demo_surf = pygame.Surface((DISPLAY.get_width()/2 - 13, DISPLAY.get_height()), pygame.SRCALPHA)

    doc_screen = scrolling_screen.scrolling_screen(doc_surf, 2, "l", 13, 15, (230,230,230))
    back_button = button.button(doc_screen.surface, [255,255,255,150], [255,255,255,200], grid.get_column(0.06), grid.get_row(0.2), 85,35, "BACK", anim=True) 

    #TITLE
    title = text.text(doc_screen.surface, pygame.font.SysFont('arial', 40), (255,255,255))
    title.message("Button", (grid.get_column(0.5), grid.get_row(1)), center=True)

    #HEADING
    heading = text.text(doc_screen.surface, pygame.font.SysFont('arial', 35), (230,230,230))
    heading.message("Methods", (grid.get_column(0.06), grid.get_row(4.5)))
    
    #HEADING 2
    heading_2 = text.text(doc_screen.surface, pygame.font.SysFont('arial', 30), (200,200,200))
    heading_2.message("pgscript.button.button()", (grid.get_column(0.06), grid.get_row(4.8)))
    #PARAGRAPHS
    paragraph = text.text(doc_screen.surface, pygame.font.SysFont('arial', 20), (255,255,255))

    paragraph.wrapped_text("", (grid.get_column(0.06), grid.get_row(2)), 580, 2)

    #paragraph.wrapped_text("", (grid.get_column(0.06),grid.get_row(5.5)))


     
    doc_screen.add_objects([title, heading, heading_2, paragraph, back_button])

    background = bg.parallax_bg(doc_surf, "obj_bg.jpg") 

    while not back_button.get_state():
        pygame.display.update()
        background.draw()

        demo_surf.fill([200,200,200,200])
        doc_screen.surface.fill([255,255,255,0])

        doc_screen.draw()
        DISPLAY.blit(doc_surf, (0, 0))
        DISPLAY.blit(demo_surf, (grid.get_column(1) + 13, 0))

        for event in pygame.event.get():
            doc_screen.update(event)
