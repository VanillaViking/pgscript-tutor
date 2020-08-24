import pygame
from pgscript import draw_grid
from pgscript import scrolling_screen
from pgscript import text
from pgscript import bg
from pgscript import button
from pgscript import text_input

from pgscript_parser import parse_args

def draw(DISPLAY):
    grid = draw_grid.draw_grid(DISPLAY, 2, 8)

    doc_surf = pygame.Surface((DISPLAY.get_width(), DISPLAY.get_height()))

    demo_screen = pygame.Surface((DISPLAY.get_width()/2 - 13, DISPLAY.get_height()), pygame.SRCALPHA)

    doc_screen = scrolling_screen.scrolling_screen(doc_surf, 4, "l", 13, 15, (230,230,230))
    back_button = button.button(doc_screen.surface, [255,255,255,150], [255,255,255,200], grid.get_column(0.06), grid.get_row(0.2), 85,35, "BACK", anim=True) 

    demo_button = button.button(demo_screen, (0,0,0), (75,75,75), 245, 285, 150,100, "example", (200,200,200))

    demo_text = 'demo_button = button.button(demo_screen, (0,0,0), (75,75,75), 245, 285, 150,100, "example", (200,200,200))' 
    error_text = text.text(demo_screen, pygame.font.SysFont('arial', 20), (230,0,0))

    #TITLE
    title = text.text(doc_screen.surface, pygame.font.SysFont('arial', 40), (255,255,255))
    title.message("Button", (grid.get_column(0.5), grid.get_row(1)), center=True)

    #HEADING
    heading = text.text(doc_screen.surface, pygame.font.SysFont('arial', 35), (230,230,230))
    heading.message("Methods", (grid.get_column(0.06), grid.get_row(4.5)))
    
    #HEADING 2
    heading_2 = text.text(doc_screen.surface, pygame.font.SysFont('arial', 30), (200,200,200))
    heading_2.message("pgscript.button.button()", (grid.get_column(0.06), grid.get_row(5)))
    heading_2.message("pgscript.button.draw()", (grid.get_column(0.06), grid.get_row(16.5)))
    heading_2.message("pgscript.button.update()", (grid.get_column(0.06), grid.get_row(19)))

    #PARAGRAPHS
    paragraph = text.text(doc_screen.surface, pygame.font.SysFont('arial', 20), (255,255,255))
    # 1 line: 0.6, 2 lines: 0.8, 3 lines: 0.9
    paragraph.wrapped_text("This object creates a button (pygame surface) that can be drawn onto a display surface. The object also indicates when a mouse button is pressed within the button’s boundaries.The button is drawn onto a display surface using the draw() method. To allow the button to indicate presses, the update()  method needs to be called. If the button has been pressed, the button.pressed attribute is set to true.", (grid.get_column(0.06), grid.get_row(2)), 580, 2)

    paragraph.wrapped_text("The constructor method of the button. The button’s appearance and position is passed as arguments to this constructor.", (grid.get_column(0.06),grid.get_row(6)), 580, 2)
    #args
    paragraph.wrapped_text("Display_surface: (Pygame.surface) The surface that the button needs to be drawn to. Usually this surface is the display surface of the window.", (grid.get_column(0.06),grid.get_row(6.7)), 580, 2)
    paragraph.wrapped_text("passive_color: (list [r,g,b]) The color of the button when the mouse cursor is not hovering over the button", (grid.get_column(0.06),grid.get_row(7.7)), 580, 2)
    paragraph.wrapped_text("active_color: (list [r,g,b]) the colour of the button when the mouse cursor is hovering over the button", (grid.get_column(0.06),grid.get_row(8.5)), 580, 2)
    paragraph.wrapped_text("x_postion: (int) The coordinate of the top left corner of the button on the x axis", (grid.get_column(0.06),grid.get_row(9.3)), 580, 2)
    paragraph.wrapped_text("y_position: (int) The coordinate of the top left corner of the button on the y axis", (grid.get_column(0.06),grid.get_row(10.1)), 580, 2)
    paragraph.wrapped_text("length: (int) The length (in pixels) of the button", (grid.get_column(0.06),grid.get_row(10.9)), 580, 2)
    paragraph.wrapped_text("height: (int) the height (in pixels) of the button", (grid.get_column(0.06),grid.get_row(11.5)), 580, 2)
    paragraph.wrapped_text("text_col: (list [r,g,b]) The color of the text within the button. Default value is black.", (grid.get_column(0.06),grid.get_row(12.1)), 580, 2)
    paragraph.wrapped_text("anim: (bool) If set to true, the button fades into the other color instead of instantly switching to it.", (grid.get_column(0.06),grid.get_row(12.9)), 580, 2)
    paragraph.wrapped_text("font_size: (int) size of the text in the button. Font size is set to 30 by default.", (grid.get_column(0.06),grid.get_row(13.7)), 580, 2)
    paragraph.wrapped_text("Wrapping: (int)  how many characters to wrap the text inside the button by. If the value is 0, the text will not be wrapped. Default value is 0", (grid.get_column(0.06),grid.get_row(14.5)), 580, 2)
    paragraph.wrapped_text("text_center: (bool) states whether the text inside the button should be vertically centered. Default value is true.", (grid.get_column(0.06),grid.get_row(15.5)), 580, 2)

    paragraph.wrapped_text("This method draws the button surface onto the display_surface of the object, which is set using it’s constructor method. It is meant to be called in the same loop as where display_surface is updated.", (grid.get_column(0.06),grid.get_row(17.1)), 580, 2)
    paragraph.wrapped_text("This method checks if the cursor is hovering over the button and is pressed. If the conditions are met, the button object’s pressed attribute is set to true. It is meant to be called in a loop with each pygame event given by pygame.event.get() as an argument.", (grid.get_column(0.06),grid.get_row(19.6)), 580, 2)


    heading_2.message("pgscript.button.get_state()", (grid.get_column(0.06), paragraph.text_end[1] + 70))

    paragraph.wrapped_text("This method returns true if the button has been pressed.", (grid.get_column(0.06), heading_2.text_end[1] + 20), 580, 2)

    heading_2.message("pgscript.button.reset_state()", (grid.get_column(0.06), paragraph.text_end[1] + 70))

    paragraph.wrapped_text("This method resets the button so that the get_state() method will return false until the button is pressed again. This needs to be used when the button is required to be pressable after it has already been pressed before.", (grid.get_column(0.06), heading_2.text_end[1] + 20), 580, 2)
    
    #DEMO
    #heading.message("DEMO", (grid.get_column(0.06), paragraph.text_end[1] + 70))     
    
    demo_input = text_input.text_input(demo_screen, grid.get_column(0), grid.get_row(6.5), 610, 30, demo_text, (0,0,0),(25,25,25),(100,100,100), 15)
    run_demo = button.button(demo_screen, [0,0,0,240], [0,0,0,190],grid.get_column(0.02), demo_input.rect.bottom + 10, 85,30, "Run", (200,200,200), anim=True)
    reset_demo = button.button(demo_screen, [0,0,0,240], [0,0,0,190],grid.get_column(0.02) + 90, demo_input.rect.bottom + 10, 85,30, "Reset", (200,200,200), anim=True)

    doc_screen.add_objects([title, heading, heading_2, paragraph, back_button])

    background = bg.parallax_bg(doc_surf, "obj_bg.jpg") 

    while not back_button.get_state():
        pygame.display.update()
        background.draw()

        demo_screen.fill([200,200,200,200])
        demo_button.draw()
        demo_input.draw()
        run_demo.draw()
        reset_demo.draw()
        error_text.draw()
        doc_screen.surface.fill([255,255,255,0])

        doc_screen.draw()
        DISPLAY.blit(doc_surf, (0, 0))
        DISPLAY.blit(demo_screen, (grid.get_column(1) + 13, 0))

        if run_demo.get_state():
            demo_args = demo_input.get_text()[28:-1]
            try:
                demo_button = button.button(demo_screen, *parse_args(demo_args))
                print(*parse_args(demo_args))
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
            demo_button.update(event , (pygame.mouse.get_pos()[0] - (DISPLAY.get_width()/2) - 13, pygame.mouse.get_pos()[1]))
            reset_demo.update(event, (pygame.mouse.get_pos()[0] - (DISPLAY.get_width()/2) - 13, pygame.mouse.get_pos()[1]))




