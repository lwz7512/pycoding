import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

MOVEMENT_MAX_SPEED = 10  # initial speed, V0



class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y  # current vertical speed
        self.radius = radius
        self.color = color
        self.t = 0
        self.g = 1
        self.start = False

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        """ Calculate speed & Move the ball """
        self.position_y += self.change_y  # move the ball by speed
        
        if self.start == True:
          self.change_y = MOVEMENT_MAX_SPEED - self.g * self.t
          self.t += 0.2   # time elapse

        if self.change_y < -MOVEMENT_MAX_SPEED:
          self.t = 0
          self.change_y = 0
          self.start = False



class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        # self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(320, 15, 0, 0, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()

    def update(self, delta_time):
        self.ball.update()


    def on_key_press(self, key, modifiers):

        """ Called whenever the user presses a key. """

        if key == arcade.key.SPACE:
            print('space pressed!')
            self.ball.start = True



    def on_key_release(self, key, modifiers):

        """ Called whenever a user releases a key. """

        # if key == arcade.key.LEFT or key == arcade.key.RIGHT:

        #     self.ball.change_x = 0

        # elif key == arcade.key.UP or key == arcade.key.DOWN:

        #     self.ball.change_y = 0



def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()