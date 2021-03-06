""" 
Knowledge Points:

* how to move
* move speed
* how to stop
* move inside boundary

Assignment:

* move rectangle
* move verticle
"""
import arcade


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

        # Attributes to store where our ball is
        self.ball_x = 300
        self.ball_y = 240

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        arcade.draw_circle_filled(self.ball_x, self.ball_y, 15, arcade.color.AUBURN)

    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball_x += 3
        self.ball_y += 3

def main():
    window = MyGame(640, 480, "Simple Animation")

    arcade.run()

main()
