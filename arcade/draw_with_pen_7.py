# draw real line with colorful pen
# @2020/10/03

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
        
        # add sprites or elements below this:
        self.counter = 0

        self.small_ball = Ball(50, 50, 3, arcade.color.BLACK)

        # all of points
        self.points = []

        # draw flag
        self.draw_flag = False


    def setup(self):
      # add sprite here
      pass

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        # draw pen
        self.small_ball.draw()
        # draw line by points
        for line in self.points:
          arcade.draw_line_strip(line, arcade.color.BLACK, 6)
        

    def update(self, delta_time):
        # print('>>> to update before on_draw :')
        # print(len(self.points))
        self.counter += 1


    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        # move pen
        self.small_ball.position_x = x
        self.small_ball.position_y = y
        # add each point to list
        if self.draw_flag:
          self.points[-1].append((x, y))


    def on_mouse_press(self, x, y, button, modifiers):
        self.draw_flag = True
        self.points.append([])


    def on_mouse_release(self, x, y, button, modifiers):
        self.draw_flag = False

        


def main():
    window = MyGame(640, 480, "Template Game")
    arcade.run()


main()