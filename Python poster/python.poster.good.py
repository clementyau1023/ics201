import arcade


WIDTH = 900
HEIGHT = 750

chair_x = 0

my_button = [600, 200, 200, 100]
show_text = False
show_time_limit = 20
show_time = 0

def chair(x, y):

    # chair
    arcade.draw_line(780 + x, 440, 780 + x, 385, arcade.color.JORDY_BLUE, 5)
    arcade.draw_line(777 + x, 385, 840 + x, 385, arcade.color.JORDY_BLUE, 5)
    arcade.draw_line(808.5 + x, 385, 808.5 + x, 360, arcade.color.JORDY_BLUE, 5)
    arcade.draw_line(791.5 + x, 360, 825.5 + x, 360, arcade.color.JORDY_BLUE, 5)
    arcade.draw_circle_filled(791.5 + x, 350.5, 7, arcade.color.CADMIUM_ORANGE)
    arcade.draw_circle_filled(825.5 + x, 350.5, 7, arcade.color.CADMIUM_ORANGE)


def on_update(delta_time):
    global chair_x
    chair_x += 1



    global show_time, show_text
    show_time += delta_time

    if show_time < show_time_limit and show_text:
        show_text = True
    else:
        show_text = False

def on_draw():
    arcade.start_render()

    arcade.draw_text("Computer Ergonomics", 280, 700, arcade.color.BLACK, 25)

    # ergonomics tips
    arcade.draw_text("Tips for sitting at your computer", 60, 650, arcade.color.BLACK, 15)
    arcade.draw_line(55, 645, 340, 645, arcade.color.WHITE, 2)

    # Bullet Points
    point_list = ((60, 633),
                  (60, 603),
                  (60, 573),
                  (60, 543),
                  (60,483),
                  (60, 453))
    arcade.draw_points(point_list, arcade.color.TEAL_DEER, 7)
    arcade.draw_point(85, 513, arcade.color.MEDIUM_ELECTRIC_BLUE, 5)
    arcade.draw_text("Sit upright with your back straight and shoulders back", 70, 630, arcade.color.BLACK, 12)
    arcade.draw_text("Your body should face the screen, don't twist your head or body to face the screen", 70, 600, arcade.color.BLACK, 12)
    arcade.draw_text("Use a chair that has support for your lower back, and a cushioned seat", 70, 570, arcade.color.BLACK, 12)
    arcade.draw_text("Try to work away from sunlight and windows, ", 70, 540, arcade.color.BLACK, 12)
    arcade.draw_text("If not possible position your screen so there’s minimal glare by having the screen face away from the suns’ rays", 95, 510,arcade.color.BLACK, 12)
    arcade.draw_text("Periodically stand up and walk around to prevent back strain/pain and neck strains", 70, 480, arcade.color.BLACK, 12)
    arcade.draw_text("Use a chair that has support for your lower back, and a cushioned seat", 70, 450, arcade.color.BLACK, 12)


    #images
    texture = arcade.load_texture("situp.jpg")
    scale = 0.25
    arcade.draw_texture_rectangle(760, 620, scale * texture.width,
                                  scale * texture.height, texture, 0)

    texture = arcade.load_texture("20-20-eyesights.png")
    scale = 0.2
    arcade.draw_texture_rectangle(200, 200, scale * texture.width,
                                  scale * texture.height, texture, 0)


    # stickman sitting in chair
        # body
    arcade.draw_circle_filled(700, 650, 10, arcade.color.FLIRT)
    arcade.draw_line(700, 640, 700, 600, arcade.color.FLIRT, 1.5)
    arcade.draw_line(685, 620, 715, 620, arcade.color.FLIRT, 1.5)
    arcade.draw_line(700, 600, 725, 600, arcade.color.FLIRT, 1.5)
    arcade.draw_line(700, 600, 725, 600, arcade.color.FLIRT, 1.5)
    arcade.draw_line(725,600, 740, 610, arcade.color.FLIRT,1.5)
    arcade.draw_line(725,600, 740, 590, arcade.color.FLIRT,1.5)
        # face
    arcade.draw_line(695, 655, 695, 650, arcade.color.BLACK, 1.5)
    arcade.draw_line(705, 655, 705, 650, arcade.color.BLACK, 1.5)
    arcade.draw_arc_outline(700, 646, 4, 4, arcade.color.BLACK, 180, 360)
        # chair
    arcade.draw_line(680, 640, 680, 585, arcade.color.JORDY_BLUE, 5)
    arcade.draw_line(677, 585, 740, 585, arcade.color.JORDY_BLUE, 5)
    arcade.draw_line(708.5, 585, 708.5, 560, arcade.color.JORDY_BLUE, 5)
    arcade.draw_line(691.5, 560, 725.5, 560, arcade.color.JORDY_BLUE, 5)
    arcade.draw_circle_filled(691.5, 550.5, 7, arcade.color.CADMIUM_ORANGE)
    arcade.draw_circle_filled(725.5, 550.5, 7, arcade.color.CADMIUM_ORANGE)


    # 20 20 20 rule

    arcade.draw_text("20-20-20 rule", 70, 375, arcade.color.BLACK, 15)
    arcade.draw_line(65, 370, 195, 370, arcade.color.WHITE, 2)
    arcade.draw_text("Every                       look at something                away for  ", 70, 350,
                     arcade.color.BLACK, 12)
    arcade.draw_text("           20 minutes                                  20 feet                  20 seconds", 70, 350, arcade.color.BLACK, 12, bold=True)

    # Button Hotspot
    arcade.draw_text("CLICK ME", 550, 200, arcade.color.BLACK, 20, bold=True)
    arcade.draw_rectangle_outline(my_button[0],
                                  my_button[1],
                                  my_button[2],
                                  my_button[3],
                                  arcade.color.BLACK)

    if show_text:
        arcade.draw_text(
            "Look out your windows or across the room until you see\nthis message go away in your peripheral vision",
            450, 125, arcade.color.PINE_GREEN, 12, bold=True, italic=True)


# stickman moving_chair
    # Stickman

    arcade.draw_circle_filled(800, 450, 10, arcade.color.FLIRT)
    arcade.draw_line(800, 440, 800, 400, arcade.color.FLIRT, 1.5)
    arcade.draw_line(785, 420, 815, 420, arcade.color.FLIRT, 1.5)
    arcade.draw_line(800, 400, 825, 400, arcade.color.FLIRT, 1.5)
    arcade.draw_line(800, 400, 825, 400, arcade.color.FLIRT, 1.5)
    arcade.draw_line(825, 400, 840, 410, arcade.color.FLIRT, 1.5)
    arcade.draw_line(825, 400, 840, 390, arcade.color.FLIRT, 1.5)
    # face
    arcade.draw_line(795, 455, 795, 450, arcade.color.BLACK, 1.5)
    arcade.draw_line(805, 455, 805, 450, arcade.color.BLACK, 1.5)
    arcade.draw_arc_outline(800, 446, 4, 4, arcade.color.BLACK, 180, 360)

    arcade.draw_text("Animation is supposed to depict\nman getting up from his seat", 725, 325, arcade.color.BLACK, 8)

    chair(chair_x, 50)

















def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass

def on_mouse_press(x, y, button, modifiers):
    global show_time, show_text
    my_button_x, my_button_y, my_button_w, my_button_h = my_button

    if (x > my_button_x and x < my_button_x + my_button_w and
            y > my_button_y and y < my_button_y + my_button_h):
        show_text = True
        show_time = 0  # reset show_time
    else:
        show_text = False

def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.PALE_BLUE)
    arcade.schedule(on_update, 1/10)
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press



    arcade.run()


if __name__ == '__main__':
    setup()