import pygame
from pgscript import draw_grid
from pgscript import scrolling_screen
from pgscript import text
from pgscript import bg
from pgscript import button
from pgscript import text_input
from pgscript_parser import parse_args

from pgscript import slider

def draw(DISPLAY):
    grid = draw_grid.draw_grid(DISPLAY, 2,8)

    doc_surf = pygame.Surface((DISPLAY.get_width(), DISPLAY.get_height()))# surface where text from documentation is placed

    demo_screen = pygame.Surface((DISPLAY.get_width()/2 - 13, DISPLAY.get_height()), pygame.SRCALPHA) #surface where users can experiment with the demonstration

    doc_screen = scrolling_screen.scrolling_screen(doc_surf, 2.6, "l", 13, 15, (230,230,230))
    back_button = button.button(doc_screen.surface, [255,255,255,150], [255,255,255,200], grid.get_column(0.06), grid.get_row(0.2), 85,35, "BACK", anim=True) 
    
    #DEMO OBJECTS
    demo = slider.slider(demo_screen, (0,0,0),(255,255,255), (245,285,150,25))
    demo_text = 'slider.slider(demo_screen, (0,0,0),(255,255,255), (245,285,150,25))'

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

    
    title.message("Slider", (grid.get_column(0.5), grid.get_row(1)), center=True) 

    paragraph.wrapped_text("This object allows input from a specific range of numbers. The user can slide the bar inside the rectangle to their desired value. This value can be retrieved from the slider as a percentage of the slider’s length.", (grid.get_column(0.06), title.text_end[1] + 125), 580, 2)

    heading.message("Methods", (grid.get_column(0.06), paragraph.text_end[1] + 100))

    heading_2.message("pgscript.slider.slider()", (grid.get_column(0.06), heading.text_end[1] + 100))

    paragraph.wrapped_text("Constructor method of the slider. It’s appearance and position are passed as arguments to this constructor.", (grid.get_column(0.06), heading_2.text_end[1] + 75), 580, 2)

    arg_heading.message("DISPLAY (pygame.Surface):", (grid.get_column(0.06), paragraph.text_end[1] + 50))

    paragraph.wrapped_text("The surface that the object needs to be drawn to. Usually this surface is the display surface of the window.", (arg_heading.text_end[0]+7,arg_heading.text_end[1]), 580 - arg_heading.text_end[0]-7, 2)

    arg_heading.message("colour (list [r,g,b]):", (grid.get_column(0.06), paragraph.text_end[1] + 50))

    paragraph.wrapped_text("colour of the slider bar.", (arg_heading.text_end[0]+7,arg_heading.text_end[1]), 580 - arg_heading.text_end[0]-7, 2)

    arg_heading.message("border_colour (list [r,g,b]):", (grid.get_column(0.06), paragraph.text_end[1] + 50))

    paragraph.wrapped_text("colour of the outline around the slider bar.", (arg_heading.text_end[0]+7,arg_heading.text_end[1]), 580 - arg_heading.text_end[0]-7, 2)

    arg_heading.message("rect (list (x,y,length,height)):", (grid.get_column(0.06), paragraph.text_end[1] + 50))

    paragraph.wrapped_text("Position of and size of the slider object.", (arg_heading.text_end[0]+7,arg_heading.text_end[1]), 580 - arg_heading.text_end[0]-7, 2)

    heading_2.message("pgscript.slider.draw()", (grid.get_column(0.06), paragraph.text_end[1] + 100))

    paragraph.wrapped_text("Draws the slider object onto the DISPLAY surface. This method is meant to be called in the same loop where DISPLAY is updated", (grid.get_column(0.06), heading_2.text_end[1] + 75), 580, 2)

    heading_2.message("pgscript.slider.update()", (grid.get_column(0.06), paragraph.text_end[1] + 100))

    paragraph.wrapped_text("This method uses pygame events to check for mouse positions and clicks in order to update the value of the slider.  It is meant to be run in a loop with each event given by pygame.event.get()", (grid.get_column(0.06), heading_2.text_end[1] + 75), 580, 2)

    heading_2.message("pgscript.slider.get_value()", (grid.get_column(0.06), paragraph.text_end[1] + 100))

    paragraph.wrapped_text("This method allows the program to read the value of the slider. It returns a float between 0 and 1 depending on how full the slider is.", (grid.get_column(0.06), heading_2.text_end[1] + 75), 580, 2)

    heading_2.message("pgscript.slider.set_value(value)", (grid.get_column(0.06), paragraph.text_end[1] + 100))

    paragraph.wrapped_text("This method allows the program to read the value of the slider. It returns a float between 0 and 1 depending on how full the slider is.", (grid.get_column(0.06), heading_2.text_end[1] + 75), 580, 2)
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
            demo_args = demo_input.get_text()[14:-1]
            try:
                demo = slider.slider(demo_screen, *parse_args(demo_args)) #generate the object with args in the text field
            except:
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
            demo.update(event , (pygame.mouse.get_pos()[0] - (DISPLAY.get_width()/2) - 13, pygame.mouse.get_pos()[1]))
            reset_demo.update(event, (pygame.mouse.get_pos()[0] - (DISPLAY.get_width()/2) - 13, pygame.mouse.get_pos()[1]))


