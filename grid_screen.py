import pygame
from pgscript import draw_grid
from pgscript import scrolling_screen
from pgscript import text
from pgscript import bg
from pgscript import button
from pgscript import text_input
from parser import parse_args

def draw(DISPLAY):
    grid = draw_grid.draw_grid(DISPLAY, 2,8)

    doc_surf = pygame.Surface((DISPLAY.get_width(), DISPLAY.get_height()))# surface where text from documentation is placed

    demo_screen = pygame.Surface((DISPLAY.get_width()/2 - 13, DISPLAY.get_height()), pygame.SRCALPHA) #surface where users can experiment with the demonstration

    doc_screen = scrolling_screen.scrolling_screen(doc_surf, 2.2, "l", 13, 15, (230,230,230))
    back_button = button.button(doc_screen.surface, [255,255,255,150], [255,255,255,200], grid.get_column(0.06), grid.get_row(0.2), 85,35, "BACK", anim=True) 
    
    #DEMO OBJECTS
    demo_text = 'grid = draw_grid.draw_grid(DISPLAY, 2, 8)'

    demo_input = text_input.text_input(demo_screen, grid.get_column(0), grid.get_row(6.5), 610, 30, demo_text, (0,0,0),(25,25,25),(100,100,100), 15)
    run_demo = button.button(demo_screen, [0,0,0,240], [0,0,0,190],grid.get_column(0.02), demo_input.rect.bottom + 10, 85,30, "Run", (200,200,200), anim=True)
    reset_demo = button.button(demo_screen, [0,0,0,240], [0,0,0,190],grid.get_column(0.02) + 90, demo_input.rect.bottom + 10, 85,30, "Reset", (200,200,200), anim=True)

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
 
    title.message("Draw Grid", (grid.get_column(0.5), grid.get_row(1)), center=True) 

    paragraph.wrapped_text("The draw grid is a tool that aims to simplify the placement of objects on the display surface. As the name suggests, this tool creates an imaginary grid that users can take as reference points to place objects on the screen. For example, if you wanted three objects alongside each other, you could use the grid function and attach them to the same row, but on different columns.", (grid.get_column(0.06), title.text_end[1] + 125), 580, 2)

    heading.message("Methods", (grid.get_column(0.06), paragraph.text_end[1] + 100))

    heading_2.message("pgscript.draw_grid.draw_grid()", (grid.get_column(0.06), heading.text_end[1] + 100))

    paragraph.wrapped_text("The constructor method of the class. The number of rows and columns that the user requires in the grid is passed as an argument here.", (grid.get_column(0.06), heading_2.text_end[1] + 75), 580, 2)

    arg_heading.message("DISPLAY (pygame.Surface):", (grid.get_column(0.06), paragraph.text_end[1] + 50))

    paragraph.wrapped_text("The surface that the object needs to be drawn to. Usually this surface is the display surface of the window.", (arg_heading.text_end[0]+7,arg_heading.text_end[1]), 580 - arg_heading.text_end[0]-7, 2)

    arg_heading.message("columns (int):", (grid.get_column(0.06), paragraph.text_end[1] + 50))
    paragraph.wrapped_text("number of columns needed in the grid", (arg_heading.text_end[0]+7,arg_heading.text_end[1]), 580 - arg_heading.text_end[0]-7, 2)

    arg_heading.message("rows (int)", (grid.get_column(0.06), paragraph.text_end[1] + 50))
    paragraph.wrapped_text("number of rows needed in the grid", (arg_heading.text_end[0]+7,arg_heading.text_end[1]), 580 - arg_heading.text_end[0]-7, 2)


    heading_2.message("pgscript.text.get_row(row)", (grid.get_column(0.06), paragraph.text_end[1] + 100))

    paragraph.wrapped_text("returns the y position of the specified row", (grid.get_column(0.06),heading_2.text_end[1] +75), 580, 2)


    heading_2.message("pgscript.text.get_column(col)", (grid.get_column(0.06), paragraph.text_end[1] + 100))

    paragraph.wrapped_text("returns the x position of the specified column", (grid.get_column(0.06),heading_2.text_end[1] +75), 580, 2)

    heading_2.message("pgscript.text.wrapped_text()", (grid.get_column(0.06), paragraph.text_end[1] + 100))

    paragraph.wrapped_text("This method is used to make displaying large amounts of texts such as paragraphs easier in pygame.", (grid.get_column(0.06),heading_2.text_end[1] +75), 580, 2)




    #--------------------------------------------------------------------------------

    error_text.message("Demo unavailable.", (grid.get_column(0.5), grid.get_row(7)), 0, center=True)
    background = bg.parallax_bg(doc_surf, "obj_bg.jpg") 
    doc_screen.add_objects([title, heading, heading_2,arg_heading, paragraph, back_button])
    while not back_button.get_state():
        pygame.display.update()
        background.draw()

        demo_screen.fill([200,200,200,200])
        #demo.draw()
        demo_input.draw()
        #run_demo.draw()
        #reset_demo.draw()
        error_text.draw()
        doc_screen.surface.fill([255,255,255,0])

        doc_screen.draw()
        DISPLAY.blit(doc_surf, (0, 0))
        DISPLAY.blit(demo_screen, (grid.get_column(1) + 13, 0))

        if run_demo.get_state():
            demo_args = demo_input.get_text()[29:-1]
            print(demo_args)
            try:
                demo = title.message(*parse_args(demo_args)) #generate the object with args in the text field
            except:
                error_text.message("Invalid syntax", (grid.get_column(0.5), grid.get_row(7)), 3, center=True)
            run_demo.reset_state()
        elif reset_demo.get_state():
            demo_input.set_text(demo_text)
            run_demo.pressed = True
            reset_demo.reset_state()

        for event in pygame.event.get():
            doc_screen.update(event)
            #run_demo.update(event, (pygame.mouse.get_pos()[0] - (DISPLAY.get_width()/2) - 13, pygame.mouse.get_pos()[1]))
            #demo_input.update(event, (pygame.mouse.get_pos()[0] - (DISPLAY.get_width()/2) - 13, pygame.mouse.get_pos()[1]))
            #demo.update(event , (pygame.mouse.get_pos()[0] - (DISPLAY.get_width()/2) - 13, pygame.mouse.get_pos()[1]))
            #reset_demo.update(event, (pygame.mouse.get_pos()[0] - (DISPLAY.get_width()/2) - 13, pygame.mouse.get_pos()[1]))


