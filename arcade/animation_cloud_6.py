import arcade


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

        self.cloud_x = 200
        self.cloud_y = 370
        self.speed = 6


    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()

        arcade.draw_lrtb_rectangle_filled(0, 640, 480, 100, arcade.csscolor.BLUE)
        # Draw a rectangle
        # Left of 0, right of 599
        # Top of 300, bottom of 0
        arcade.draw_lrtb_rectangle_filled(0, 640, 100, 0, arcade.csscolor.GREEN)
        # Tree trunk
        # Center of 100, 320
        # Width of 20
        # Height of 60
        arcade.draw_rectangle_filled(100, 120, 20, 60, arcade.csscolor.SIENNA)
        # Tree top
        arcade.draw_circle_filled(100, 150, 30, arcade.csscolor.DARK_GREEN)
        # Another tree, with a trunk and ellipse for top
        arcade.draw_rectangle_filled(200, 120, 20, 60, arcade.csscolor.SIENNA)
        arcade.draw_ellipse_filled(200, 170, 60, 80, arcade.csscolor.DARK_GREEN)
        # Another tree, with a trunk and arc for top
        # Arc is centered at (300, 340) with a width of 60 and height of 100.
        # The starting angle is 0, and ending angle is 180.
        arcade.draw_rectangle_filled(300, 120, 20, 60, arcade.csscolor.SIENNA)
        arcade.draw_arc_filled(300, 140, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

        # cloud
        arcade.draw_ellipse_filled(self.cloud_x, self.cloud_y, 100, 30, arcade.csscolor.WHITE)

    def update(self, delta_time):
      self.cloud_x += self.speed

      if self.cloud_x > 640 - 50 or self.cloud_x < 50:
          self.speed = -self.speed


def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()
