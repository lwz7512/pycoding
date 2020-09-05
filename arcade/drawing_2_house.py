import arcade


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()

        arcade.draw_lrtb_rectangle_filled(0, 640, 480, 100, arcade.csscolor.BLUE)
        # Draw a rectangle
        # Left of 0, right of 599
        # Top of 300, bottom of 0
        arcade.draw_lrtb_rectangle_filled(0, 640, 100, 0, arcade.csscolor.GREEN)

        # house base
        arcade.draw_rectangle_filled(200, 150, 150, 100, arcade.csscolor.WHEAT)

        # chimney
        arcade.draw_rectangle_filled(160, 260, 18, 44, arcade.csscolor.GRAY)

        # house top
        self.draw_house_top(120, 300, 80, 100)

        # house door
        arcade.draw_rectangle_filled(240, 120, 20, 40, arcade.csscolor.SIENNA)
        arcade.draw_circle_filled(245, 115, 3, arcade.color.WHITE)

        # house window
        arcade.draw_rectangle_filled(180, 160, 44, 44, arcade.csscolor.WHITE)
        arcade.draw_line(158, 160, 202, 160, arcade.color.BLACK, 1)
        arcade.draw_line(180, 182, 180, 138, arcade.color.BLACK, 1)

        # cloud
        arcade.draw_ellipse_filled(400, 410, 100, 30, arcade.csscolor.WHITE)
        arcade.draw_ellipse_filled(450, 390, 60, 30, arcade.csscolor.WHITE)

        # draw tree
        self.draw_pine_tree(330, 230)
        self.draw_pine_tree(380, 230)
        

    def draw_house_top(self, x, y, width, height):
      """
      This function draws a pine tree at the specified location.
      """
      # Draw the triangle on top of the trunk
      arcade.draw_triangle_filled(x + width, y,  # top point
                                  x, y - height, # left point
                                  x + 2*width, y - height, # right point
                                  arcade.color.DARK_GREEN)


    def draw_pine_tree(self, x, y):
      """
      This function draws a pine tree at the specified location.
      """
      # Draw the triangle on top of the trunk
      arcade.draw_triangle_filled(x + 40, y,
                                  x, y - 100,
                                  x + 80, y - 100,
                                  arcade.color.DARK_GREEN)

      # Draw the trunk
      arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 140,
                                      arcade.color.DARK_BROWN)



def main():
    window = MyGame(640, 480, "Drawing House")

    arcade.run()
    


main()
