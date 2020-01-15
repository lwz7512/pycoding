# Mariao running
# @2020/01/12


import time
import math  


# =================== Player ===============================
class Player(Actor):

  animcycle = 9
  Quadratic_Curve_A = -1
  Quadratic_Curve_B = 15
  STEP_LENGTH = 0
  STARTJUMP = False
  HSPEED = 60

  def __init__(self, startpoint, **kwargs):
    super(Player, self).__init__('mario1', **kwargs)
    self.frame = 0
    self.stp = startpoint
    self.pos = startpoint
    self.images = ['mario1', 'mario2', 'mario3']

  def update(self):
    # change skin
    self.frame = self.frame + 1
    self.image = self.images[self.frame // self.animcycle % 3]

  def move(self, dt, bounds):
    # x axis motion
    self.x += dt*self.HSPEED
    if(self.x > bounds[0]+16):
      self.x = -16
    # y axis motion
    if self.STARTJUMP:
      self._quadratic_move()
      self.x += dt*self.HSPEED*1.6 # move faster horizontally

  def _quadratic_move(self):
    self.STEP_LENGTH += .5
    y = self.Quadratic_Curve_A*self.STEP_LENGTH**2
    y += self.Quadratic_Curve_B*self.STEP_LENGTH
    realY = math.floor(y)
    if realY > 0:
      self.y = self.stp[1] - realY # y axis move
    if self.STEP_LENGTH > self.Quadratic_Curve_B:
      self.STARTJUMP = False # stop the jump
      self.STEP_LENGTH = 0 # reset the step
      self.y = self.stp[1] # restore to the init y
  
  def jump(self):
    self.STARTJUMP = True

# ========================================================




# =================== MAIN ================================
WIDTH  = 600
HEIGHT = 300

mario = Player((0, HEIGHT - 60))

def update(dt):
  mario.update()
  mario.move(dt, (WIDTH, HEIGHT))

def draw():
    screen.clear()
    screen.blit('mario-bg-600', (0, 0))
    mario.draw()

def on_key_down(key):
  if key == keys.SPACE:
    mario.jump()
    