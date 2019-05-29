import arcade


WIDTH = 900
HEIGHT = 750


def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()

    arcade.draw_text("Cloud computing", 280, 700, arcade.color.BLACK, 25)

    # About cloud computing
    arcade.draw_text("What is cloud computing?", 60, 650, arcade.color.BLACK, 15)
    arcade.draw_text("Cloud computing (The cloud) is storing and accessing data and programs via the Internet rather", 60, 625, arcade.color.BLACK, 12)
    arcade.draw_text("than on your hard drive. It is stored on remote servers, instead of than on your own computer.", 60, 607, arcade.color.BLACK, 12)

    arcade.draw_text("3 main types", 60, 575, arcade.color.BLACK, 15)

    arcade.draw_line(58, 571, 172, 571, arcade.color.BLACK, 1.5)

    # Software as a Service
    arcade.draw_text("Software as a Service (SaaS)", 75, 532, arcade.color.BLACK, 13.5)

    # Bullet Points
    point_list = ((100, 520),
                  (100, 490),
                  (100,475),
                  (100,460))
    arcade.draw_points(point_list, arcade.color.TEAL_DEER, 5)
    arcade.draw_point(120, 505, arcade.color.SELECTIVE_YELLOW, 5)

    arcade.draw_text("Allows users to connect to and use apps via the internet ", 110, 515, arcade.color.BLACK, 11)
    arcade.draw_text("Examples include email, calenders", 130, 500, arcade.color.BLACK, 11)
    arcade.draw_text("All software and infrastructure is taken care of by service provider", 110, 485, arcade.color.BLACK, 11)

    arcade.draw_text("Customers usually rent service based on month-month and connect to it online", 110, 470, arcade.color.BLACK, 11)

    arcade.draw_text("Allows organization to quickly start with minimal cost", 110, 455,arcade.color.BLACK, 11)



    # Infrastructure as a Service
    arcade.draw_text("Infrastructure as a Service (IaaS)", 75, 402, arcade.color.BLACK, 13.5)

    point_list = ((100, 390),
                  (100, 375),
                  (100, 360),
                  (100, 345),
                  (100, 330))
    arcade.draw_points(point_list, arcade.color.TEAL_DEER, 5)

    arcade.draw_text("Instant computing infrastructure", 110, 385, arcade.color.BLACK, 11)
    arcade.draw_text("You only pay for what you use", 110, 370, arcade.color.BLACK, 11)
    arcade.draw_text("Service provider manages infrastructure, customer manages the software", 110, 355, arcade.color.BLACK, 11)
    arcade.draw_text("No need to buy your own physical servers", 110, 340, arcade.color.BLACK, 11)
    arcade.draw_text("Common uses of IaaS", 110, 325, arcade.color.BLACK, 11)

    point_list = ((120, 315),
                  (120, 300))
    arcade.draw_points(point_list, arcade.color.SELECTIVE_YELLOW, 5)

    arcade.draw_text("High-performance computing", 130, 310, arcade.color.BLACK, 11)
    arcade.draw_text("Big data analysis", 130, 295, arcade.color.BLACK, 11)



    #Platform as a Service

    arcade.draw_text("Platform as a Service (PaaS)", 75, 242, arcade.color.BLACK, 13.5)

    point_list = ((100, 230),
                  (100, 215),
                  (100, 200),
                  (100, 170),
                  (100, 155))
    arcade.draw_points(point_list, arcade.color.TEAL_DEER, 5)

    point_list = ((120, 185),
                  (120, 140),
                  (120, 125))
    arcade.draw_points(point_list, arcade.color.SELECTIVE_YELLOW, 5)


    arcade.draw_text("Development and deployment in the cloud", 110, 225, arcade.color.BLACK, 11)
    arcade.draw_text("Lets you deliver simple cloud-based apps to sophisticated, cloud-enabled apps", 110, 210, arcade.color.BLACK, 11)
    arcade.draw_text("Includes features of  IaaS (infrastructure—servers, storage, and networking)", 110, 195, arcade.color.BLACK, 11)
    arcade.draw_text("Additionally includes middleware, development tools, business intelligence services, database management systems", 130, 180, arcade.color.BLACK, 11)
    arcade.draw_text("You manage the applications and services you develop, and the cloud service provider manages everything else", 110, 165, arcade.color.BLACK, 11)
    arcade.draw_text("Common uses of PaaS ", 110, 150, arcade.color.BLACK, 11)
    arcade.draw_text("Development framework, develop or customize cloud based apps", 130, 134, arcade.color.BLACK, 11)
    arcade.draw_text("Analytics or business intelligence, forecast product success, investment returns", 130, 120, arcade.color.BLACK, 11)



def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()