import arcade


WIDTH = 900
HEIGHT = 750


def on_update(delta_time):
    pass


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
    arcade.draw_texture_rectangle(500, 200, scale * texture.width,
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



















def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.PALE_BLUE)
    arcade.schedule(on_update, 1/60)
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press



    arcade.run()


if __name__ == '__main__':
    setup()