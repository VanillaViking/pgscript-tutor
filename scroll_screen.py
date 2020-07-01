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

    doc_screen = scrolling_screen.scrolling_screen(doc_surf, 3.2, "l", 13, 15, (230,230,230))
    back_button = button.button(doc_screen.surface, [255,255,255,150], [255,255,255,200], grid.get_column(0.06), grid.get_row(0.2), 85,35, "BACK", anim=True) 
    
    #DEMO OBJECTS
    demo_display = pygame.Surface((600,337), pygame.SRCALPHA)

    demo = scrolling_screen.scrolling_screen(demo_display, 2.5, 'r', 10, 15, (255,255,255))
    demo_text = 'demo = scrolling_screen.scrolling_screen(demo_display, 2.5, "r", 10, 15, (255,255,255))'

    d_head = text.text(demo.surface, pygame.font.SysFont('arial', 35), (230,230,230))
    d_head.message("Example", (300, int(337/2)),0, True )

    demo.add_objects([d_head])

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
    title.message("Parallax Background", (grid.get_column(0.5), grid.get_row(1)), center=True) 

    paragraph.wrapped_text("This object shifts the background based on mouse movements to simulate a parallax effect. The parallax background does not need an update method since the mouse movements are used directly within the draw method.", (grid.get_column(0.06), title.text_end[1] + 125), 580, 2)

    heading.message("Methods", (grid.get_column(0.06), paragraph.text_end[1] + 100))

    heading_2.message("pgscript.bg.parallax_bg()", (grid.get_column(0.06), heading.text_end[1] + 100))

    paragraph.wrapped_text("Constructor method of the parallax background class. The path to the background image is passed as an argument to this method.", (grid.get_column(0.06), heading_2.text_end[1] + 75), 580, 2)

    arg_heading.message("DISPLAY (pygame.Surface):", (grid.get_column(0.06), paragraph.text_end[1] + 50))

    paragraph.wrapped_text("The surface that the object needs to be drawn to. Usually this surface is the display surface of the window.", (arg_heading.text_end[0]+7,arg_heading.text_end[1]), 580 - arg_heading.text_end[0]-7, 2)

    arg_heading.message("image_path (string):", (grid.get_column(0.06), paragraph.text_end[1] + 50))

    paragraph.wrapped_text("The relative path to the background image.", (arg_heading.text_end[0]+7,arg_heading.text_end[1]), 580 - arg_heading.text_end[0]-7, 2)

    arg_heading.message("ratio (float):", (grid.get_column(0.06), paragraph.text_end[1] + 50))

    paragraph.wrapped_text("how much to scale the image by in relation to the display surface. Dictates how sensitive the background will be to mouse movements", (arg_heading.text_end[0]+7,arg_heading.text_end[1]), 580 - arg_heading.text_end[0]-7, 2)


    heading_2.message("pgscript.parallax_bg.draw()", (grid.get_column(0.06), paragraph.text_end[1] + 100))

    paragraph.wrapped_text("Draws the background onto the DISPLAY surface. This method is meant to be called in the same loop where DISPLAY is updated.", (grid.get_column(0.06),heading_2.text_end[1] +75), 580, 2)



 
#--------------------------------------------------------------------------------

    background = bg.parallax_bg(doc_surf, "obj_bg.jpg") 
    doc_screen.add_objects([title, heading, heading_2,arg_heading, paragraph, back_button])
    while not back_button.get_state():
        pygame.display.update()
        background.draw()

        demo_screen.fill([200,200,200,200])
        #demo_display.fill((0,0,0,0))
        demo_screen.blit(demo_display, (13, grid.get_row(1.5)))
        demo.surface.fill([0,0,0])
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
            demo_args = demo_input.get_text()[42:-1]
            print(demo_args)
            try:
                demo = scrolling_screen.scrolling_screen(demo_display, *parse_args(demo_args)) #generate the object with args in the text field
                d_head = text.text(demo.surface, pygame.font.SysFont('arial', 35), (230,230,230))
                d_head.message("Example", (300, int(337/2)),0, True )

                demo.add_objects([d_head])
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
            demo.update(event)
            reset_demo.update(event, (pygame.mouse.get_pos()[0] - (DISPLAY.get_width()/2) - 13, pygame.mouse.get_pos()[1]))




