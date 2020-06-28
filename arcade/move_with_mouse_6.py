import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Ball:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.small_ball = Ball(50, 50, 10, arcade.color.BLACK)
        self.ball = Ball(70, 70, 15, arcade.color.AUBURN)
        self.large_ball = Ball(100, 100, 20, arcade.color.GREEN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.large_ball.draw()
        self.ball.draw()
        self.small_ball.draw()


    def on_mouse_motion(self, x, y, dx, dy):

        """ Called to update our objects. Happens approximately 60 times per second."""

        print('x: '+str(x), 'y: '+str(y))

        self.small_ball.position_x = x
        self.small_ball.position_y = y
        
        self.ball.position_x = x + 20
        self.ball.position_y = y + 20

        self.large_ball.position_x = x + 50
        self.large_ball.position_y = y + 50



def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()