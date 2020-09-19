import arcade

# teaching @2020/0912
# assignment: change ball to rectangle

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

        # Attributes to store where our ball is
        self.ball_x = 300
        self.ball_y = 240
        # ball speed
        self.ball_speed_x = 6
        self.ball_speed_y = 6

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        arcade.draw_circle_filled(self.ball_x, self.ball_y, 15, arcade.color.AUBURN)

    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball_x += self.ball_speed_x
        self.ball_y += self.ball_speed_y
        # move back when beyond the window area
        if self.ball_x > 640 or self.ball_x < 0:
          self.ball_speed_x = -self.ball_speed_x


def main():
    window = MyGame(640, 480, "Simple Animation")

    arcade.run()

main()
