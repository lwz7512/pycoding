import arcade
import math


# a = 250
# b = 150


def calculateEllipsePts(a, b):
  xList = list(range(0, a+1))
  sectionsLeft = []
  sectionsRight= []

  # first area
  for x in xList:
    y = math.sqrt(1 - (x/a)**2)*b
    sectionsLeft.append((x, y))
    # print((x, y))

  # second area
  xList.reverse()

  for x in xList:
    y = math.sqrt(1 - (x/a)**2)*b
    sectionsLeft.append((x, -y))
    # print((x, -y))

  for pt in sectionsLeft:
    sectionsRight.append((-pt[0], -pt[1]))

  sectionsLeft.extend(sectionsRight)

  return sectionsLeft


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


class MyGame(arcade.Window):

  def __init__(self, width, height, title):

     # Call the parent class's init function
    super().__init__(width, height, title)
    # Set the background color
    arcade.set_background_color(arcade.color.BLACK)
    self.centralX = 300
    self.centralY = 240
    self.sun = Ball(self.centralX, self.centralY, 50, arcade.color.RED)
    self.a = 250
    self.b = 150
    self.i = 0
    self.earthTracks = calculateEllipsePts(self.a, self.b)
    self.earth = Ball(self.centralX, self.centralY+self.b, 15, arcade.color.BLUEBERRY)


  def on_draw(self):
    """ Called whenever we need to draw the window. """
    arcade.start_render()
    self.sun.draw()
    self.earth.draw()

  def update(self, delta_time):
    """ Called to update our objects. Happens approximately 60 times per second."""
    self.i += 1
    if self.i > len(self.earthTracks) - 1 :
      self.i = 0

    earthX = self.earthTracks[self.i][0]
    earthY = self.earthTracks[self.i][1]
    self.earth.update(self.centralX+earthX, self.centralY+earthY)


def main():
    window = MyGame(640, 480, "Solor System")

    arcade.run()

main()