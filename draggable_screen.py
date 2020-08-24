import pygame
from pgscript import draw_grid
from pgscript import scrolling_screen
from pgscript import text
from pgscript import bg
from pgscript import button
from pgscript import text_input
from pgscript_parser import parse_args

from pgscript import draggable_surface

def draw(DISPLAY):
    grid = draw_grid.draw_grid(DISPLAY, 2,8)

    doc_surf = pygame.Surface((DISPLAY.get_width(), DISPLAY.get_height()))# surface where text from documentation is placed

    demo_screen = pygame.Surface((DISPLAY.get_width()/2 - 13, DISPLAY.get_height()), pygame.SRCALPHA) #surface where users can experiment with the demonstration

    doc_screen = scrolling_screen.scrolling_screen(doc_surf, 2.6, "l", 13, 15, (230,230,230))
    back_button = button.button(doc_screen.surface, [255,255,255,150], [255,255,255,200], grid.get_column(0.06), grid.get_row(0.2), 85,35, "BACK", anim=True) 
    
    #DEMO OBJECTS
    demo_surface = pygame.Surface((100,100))
    demo_surface.fill((0,0,0))

    demo = draggable_surface.draggable_surface(demo_screen, demo_surface, (245,285))
    demo_text = 'draggable_surface.draggable_surface(demo_screen, demo_surface, (245,285))'

    demo_input = text_input.text_input(demo_screen, grid.get_column(0), grid.get_row(6.5), 610, 30, demo_text, (0,0,0),(25,25,25),(100,100,100), 15)
    run_demo = button.button(demo_screen, [255,255,255,150], [255,255,255,200],grid.get_column(0.02), demo_input.rect.bottom + 10, 85,30, "Run" )
    reset_demo = button.button(demo_screen, [255,255,255,150], [255,255,255,200],grid.get_column(0.02) + 90, demo_input.rect.bottom + 10, 85,30, "Reset")

    #ERROR
    error_text = text.text(demo_screen, pygame.font.SysFont('arial', 20), (230,0,0))


    #TITLE
    title = text.text(doc_screen.surface, pygame.font.SysFont('arial', 40), (255,255,255))
 
    #HEADING
    heading = text.text(doc_screen.surface, pygame.font.SysFont('arial', 35), (230,230,230))
 
    #HEADING 2
    heading_2 = text.text(doc_screen.surface, pygame.font.SysFont('arial', 30), (200,200,200))
 
    #PARAGRAPHS
    paragraph = text.text(doc_screen.surface, pygame.font.SysFont('arial', 20), (255,255,255))

    #ARGUMENTS
    arg_heading = text.text(doc_screen.surface, pygame.font.SysFont('arial', 20), (255,255,255))
    arg_heading.font.set_underline(True)
    
    
#--------------------------------------------------------------------------------

    title.message("Draggable Surface", (grid.get_column(0.5), grid.get_row(1)), center=True) 

    paragraph.wrapped_text("This class creates a pygame surface that can be moved with the mouse by clicking and dragging.", (grid.get_column(0.06), title.text_end[1] + 125), 580, 2)

    heading.message("Methods", (grid.get_column(0.06), paragraph.text_end[1] + 100))

    heading_2.message("pgscript.draggable_surface()", (grid.get_column(0.06), heading.text_end[1] + 100))

    paragraph.wrapped_text("Constructor method of the class. The surface that needs to be made movable and its starting position is passed to this method as arguments.", (grid.get_column(0.06), heading_2.text_end[1] + 75), 580, 2)

    arg_heading.message("DISPLAY (pygame.Surface):", (grid.get_column(0.06), paragraph.text_end[1] + 50))

    paragraph.wrapped_text("The surface that the object needs to be drawn to. Usually this surface is the display surface of the window.", (arg_heading.text_end[0]+7,arg_heading.text_end[1]), 580 - arg_heading.text_end[0]-7, 2)

    arg_heading.message("Suface (pygame.Surface):", (grid.get_column(0.06), paragraph.text_end[1] + 50))
    
    paragraph.wrapped_text("The surface that needs to be made movable.", (arg_heading.text_end[0]+7,arg_heading.text_end[1]), 580 - arg_heading.text_end[0]-7, 2)

    arg_heading.message("start_pos (tuple (x,y)):", (grid.get_column(0.06), paragraph.text_end[1] + 50))

    paragraph.wrapped_text("The position at which the surface is initially drawn.", (arg_heading.text_end[0]+7,arg_heading.text_end[1]), 580 - arg_heading.text_end[0]-7, 2)

    heading_2.message("pgscript.draggable_surface.draw()", (grid.get_column(0.06), paragraph.text_end[1] + 100))

    paragraph.wrapped_text("Draws the draggable surface object onto the DISPLAY surface. This method is meant to be called in the same loop where DISPLAY is updated", (grid.get_column(0.06),heading_2.text_end[1] +75), 580, 2)

    heading_2.message("pgscript.draggable_surface.update(event)", (grid.get_column(0.06), paragraph.text_end[1] + 100))

    paragraph.wrapped_text("Pygame events are used to check for mouse activity and clicks.  It is meant to be run in a loop with each event given by pygame.event.get()", (grid.get_column(0.06),heading_2.text_end[1] +75), 580, 2)

    heading_2.message("pgscript.draggable_surface.get_pos()", (grid.get_column(0.06), paragraph.text_end[1] + 100))

    paragraph.wrapped_text("Returns a tuple (x,y) of the current coordinates of the surface.", (grid.get_column(0.06),heading_2.text_end[1] +75), 580, 2)

    heading_2.message("pgscript.draggable_surface.set_pos(pos)", (grid.get_column(0.06), paragraph.text_end[1] + 100))

    paragraph.wrapped_text("Sets the position of the draggable surface to pos", (grid.get_column(0.06),heading_2.text_end[1] +75), 580, 2)

    arg_heading.message("pos (tuple (x,y)):", (grid.get_column(0.06), paragraph.text_end[1] + 50))

    paragraph.wrapped_text("New desired position of the object.", (arg_heading.text_end[0] + 7,arg_heading.text_end[1]), 580, 2)

#--------------------------------------------------------------------------------

    background = bg.parallax_bg(doc_surf, "obj_bg.jpg") 
    doc_screen.add_objects([title, heading, heading_2,arg_heading, paragraph, back_button])
    while not back_button.get_state():
        pygame.display.update()
        background.draw()

        demo_screen.fill([200,200,200,200])
        demo.draw()
        demo_input.draw()
        run_demo.draw()
        reset_demo.draw()
        error_text.draw()
        doc_screen.surface.fill([255,255,255,0])

        doc_screen.draw()
        DISPLAY.blit(doc_surf, (0, 0))
        DISPLAY.blit(demo_screen, (grid.get_column(1) + 13, 0))

        if run_demo.get_state():
            demo_args = demo_input.get_text()[48:-1]
            print(demo_args)
            try:
                demo = draggable_surface.draggable_surface(demo_screen, demo_surface, *parse_args(demo_args)) #generate the object with args in the text field
            except:
                print(*parse_args(demo_args))
                error_text.message("Invalid syntax", (grid.get_column(0.5), grid.get_row(7)), 3, center=True)
            run_demo.reset_state()
        elif reset_demo.get_state():
            demo_input.set_text(demo_text)
            run_demo.pressed = True
            reset_demo.reset_state()

        for event in pygame.event.get():
            doc_screen.update(event)
            run_demo.update(event, (pygame.mouse.get_pos()[0] - (DISPLAY.get_width()/2) - 13, pygame.mouse.get_pos()[1]))
            demo_input.update(event, (pygame.mouse.get_pos()[0] - (DISPLAY.get_width()/2) - 13, pygame.mouse.get_pos()[1]))
            if pygame.mouse.get_pos()[0] > (DISPLAY.get_width()/2) +13:
                demo.update(event , (pygame.mouse.get_pos()[0] - (DISPLAY.get_width()/2) - 13, pygame.mouse.get_pos()[1]))
            else:
                demo.active = False
            reset_demo.update(event, (pygame.mouse.get_pos()[0] - (DISPLAY.get_width()/2) - 13, pygame.mouse.get_pos()[1]))


