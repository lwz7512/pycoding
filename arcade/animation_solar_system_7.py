# TODO: Earch circling with Sun

import arcade
import math


class Ball:
    """ This class manages a ball bouncing on the screen. """

    def __init__(self, position_x, position_y, radius, color):
        """ Constructor. """

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self, nx = 0, ny = 0):
        """ Code to control the ball's movement. """
        self.position_x = nx
        self.position_y = ny


class Earth(Ball):

    def __init__(self, position_x, position_y, radius, color):
        """ Constructor. """
        super().__init__(position_x, position_y, radius, color)
        self.distance = 30
        self.moonX = self.position_x+self.distance
        self.moonY = self.position_y
        self.moonAngle = 0
        self.moonSpeed = 2

    def draw(self):
        super().draw()
        arcade.draw_circle_filled(self.moonX, self.moonY, 5, arcade.color.WHITE)

    def update(self, nx = 0, ny = 0):
        super().update(nx, ny)
        self.moonAngle += self.moonSpeed
        mrad = math.radians(self.moonAngle)
        diffX = self.distance * math.cos(mrad)
        diffY = self.distance * math.sin(mrad)
        self.moonX = self.position_x + diffX
        self.moonY = self.position_y + diffY
        

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

        self.centralX = 300
        self.centralY = 240
        self.distance_sun_to_earth = 150
        self.earthAngle = 0
        self.earthSpeed = 1
        
        self.earthX = self.centralX+self.distance_sun_to_earth
        self.earthY = self.centralY
        
        self.sun = Ball(self.centralX, self.centralY, 50, arcade.color.YELLOW)
        self.earth = Earth(self.earthX, self.earthY, 15, arcade.color.BLUEBERRY)


    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.sun.draw()
        self.earth.draw()
        

    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.earthAngle += self.earthSpeed
        erad = math.radians(self.earthAngle)
        earthX = self.distance_sun_to_earth * math.cos(erad)
        earthY = self.distance_sun_to_earth * math.sin(erad)
        self.earth.update(self.centralX+earthX, self.centralY+earthY)



def main():
    window = MyGame(640, 480, "Solor System")

    arcade.run()

main()
