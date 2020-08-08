import arcade
import math




class Circle:
  """ plain circle """
  def __init__(self, position_x, position_y, radius, color):
    self.position_x = position_x
    self.position_y = position_y
    self.radius = radius
    self.color = color

  def draw(self):
    arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color, 2)
    
  def update(self):
    pass


class Roulette:
  """ Roulette class"""

  def __init__(self, position_x, position_y, radius, color):
    self.position_x = position_x
    self.position_y = position_y
    self.radius = radius
    self.color = color
    self.angle = 0
    self.max_speed = 12
    self.speed_zero = 0
    self.current_speed = 0
    self.accelerate = 0
    self.t = 0
    self.run = False

  def draw(self):
    arcade.draw_circle_outline(self.position_x, self.position_y, self.radius, self.color, 2)

    mRad = math.radians(self.angle)

    end_x = self.position_x + self.radius * math.cos(mRad)
    end_y = self.position_y + self.radius * math.sin(mRad)
    arcade.draw_line(self.position_x, self.position_y, end_x, end_y, arcade.color.BLUE, 2)

    sec_x = self.position_x + self.radius * math.cos(mRad + math.pi/2)
    sec_y = self.position_y + self.radius * math.sin(mRad + math.pi/2)
    arcade.draw_line(self.position_x, self.position_y, sec_x, sec_y, arcade.color.BLUE, 2)

    thd_x = self.position_x + self.radius * math.cos(mRad + math.pi)
    thd_y = self.position_y + self.radius * math.sin(mRad + math.pi)
    arcade.draw_line(self.position_x, self.position_y, thd_x, thd_y, arcade.color.BLUE, 2)

    fou_x = self.position_x + self.radius * math.cos(mRad + math.pi*1.5)
    for_y = self.position_y + self.radius * math.sin(mRad + math.pi*1.5)
    arcade.draw_line(self.position_x, self.position_y, fou_x, for_y, arcade.color.BLUE, 2)


  def update(self):
    if not self.run:
      return

    self.t += 0.2
    new_speed = self.speed_zero + self.accelerate * self.t
    
    if new_speed > self.max_speed:
      new_speed = self.max_speed
    if new_speed < 0:
      new_speed = 0
      self.run = False

    self.angle -= new_speed
    self.current_speed = new_speed


  def start(self):
    self.run = True
    self.t = 0
    self.speed_zero = 0
    self.accelerate = 1


  def stop(self):
    self.t = 0
    self.speed_zero = self.current_speed
    self.accelerate = -1


class Button:
  """ Button class """

  def __init__(self, position_x, position_y, width, height, color, solid = False):
    self.position_x = position_x
    self.position_y = position_y
    self.width = width
    self.height = height
    self.color = color
    self.solid = solid

  def draw(self):
    if self.solid: 
      arcade.draw_lrtb_rectangle_filled(self.position_x, self.position_x + self.width, self.position_y, self.position_y-self.height, self.color)
    else:
      arcade.draw_lrtb_rectangle_outline(self.position_x, self.position_x + self.width, self.position_y, self.position_y-self.height, self.color, 1)

  def update(self):
    pass

  def isTouched(self, x, y):
    in_hori_section = False
    if x > self.position_x and x < self.position_x + self.width:
      in_hori_section = True
    in_vert_section = False
    if y > self.position_y - self.height and y < self.position_y:
      in_vert_section = True
    if in_hori_section and in_vert_section:
      return True
    else:
      return False


# ----------- Game -----------------
class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
      super().__init__(width, height, title)
      arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
      self.rlt = Roulette(300, 250, 100, arcade.color.BLUE)
      self.center = Circle(300, 250, 10, arcade.color.GRAY)

      self.btn_1 = Button(150, 100, 100, 40, arcade.color.RED, False)
      self.btn_1s = Button(154, 96, 92, 32, arcade.color.RED, True)

      self.btn_2 = Button(350, 100, 100, 40, arcade.color.GREEN, False)
      self.btn_2s = Button(354, 96, 92, 32, arcade.color.GREEN, True)


    def on_draw(self):
      arcade.start_render()

      self.rlt.draw()
      self.center.draw()

      self.btn_1.draw()
      self.btn_1s.draw()

      self.btn_2.draw()
      self.btn_2s.draw()


    def on_mouse_press(self, x, y, button, modifiers):

      if self.btn_1.isTouched(x, y):
        self.rlt.start()

      if self.btn_2.isTouched(x, y):
        self.rlt.stop()

    def update(self, delta_time):
      self.rlt.update()



def main():
    window = MyGame(640, 480, "Solor System")
    window.setup()

    arcade.run()

main()
