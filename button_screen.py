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
    heading_2.message("pgscript.button.button()", (grid.get_column(0.06), grid.get_row(5)))
    #PARAGRAPHS
    paragraph = text.text(doc_screen.surface, pygame.font.SysFont('arial', 20), (255,255,255))
    # 1 line: 0.5, 2 lines: 0.7, 3 lines: 0.8
    paragraph.wrapped_text("This object creates a button (pygame surface) that can be drawn onto a display surface. The object also indicates when a mouse button is pressed within the button’s boundaries.The button is drawn onto a display surface using the draw() method. To allow the button to indicate presses, the update()  method needs to be called. If the button has been pressed, the button.pressed attribute is set to true.", (grid.get_column(0.06), grid.get_row(2)), 580, 2)

    paragraph.wrapped_text("The constructor method of the button. The button’s appearance and position is passed as arguments to this constructor.", (grid.get_column(0.06),grid.get_row(6)), 580, 2)
    #args
    paragraph.wrapped_text("Display_surface: (Pygame.surface) The surface that the button needs to be drawn to. Usually this surface is the display surface of the window.", (grid.get_column(0.06),grid.get_row(6.7)), 580, 2)
    paragraph.wrapped_text("passive_color: (list [r,g,b]) The color of the button when the mouse cursor is not hovering over the button", (grid.get_column(0.06),grid.get_row(7.7)), 580, 2)
    paragraph.wrapped_text("active_color: (list [r,g,b]) the colour of the button when the mouse cursor is hovering over the button", (grid.get_column(0.06),grid.get_row(8.4)), 580, 2)
    paragraph.wrapped_text("x_postion: (int) The coordinate of the top left corner of the button on the x axis", (grid.get_column(0.06),grid.get_row(9.1)), 580, 2)
    paragraph.wrapped_text("y_position: (int) The coordinate of the top left corner of the button on the y axis", (grid.get_column(0.06),grid.get_row(9.8)), 580, 2)
    paragraph.wrapped_text("length: (int) The length (in pixels) of the button", (grid.get_column(0.06),grid.get_row(10.5)), 580, 2)


     
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
