# first Pygame-zero project
# @2020/01/08

# from pygame import Surface, Rect
# from pygame.constants import HWSURFACE, SRCALPHA



# ======== Player =============
class Player(Actor):

  HSPEED = 0

  def __init__(self, startpoint, **kwargs):
    super(Player, self).__init__('ship_s', **kwargs)
    self.frame = 0
    self.pos = startpoint

  def move(self, dt, bounds):
    if self.x + self.HSPEED > 20 and self.x + self.HSPEED < bounds[0]-20:
      self.x += self.HSPEED

  def toLeft(self):
    self.HSPEED = -4

  def toRight(self):
    self.HSPEED = 4
  
  def stopMove(self):
    self.HSPEED = 0


# ======== Alien UFO ==========
class Alien(Actor):

  animcycle = 9
  HSPEED = 90

  def __init__(self, startpoint, **kwargs):
    super(Alien, self).__init__('alien1', **kwargs)
    self.frame = 0
    self.pos = startpoint
    self.images = ['alien1', 'alien2', 'alien3']

  def update(self):
    # change skin
    self.frame = self.frame + 1
    self.image = self.images[self.frame // self.animcycle % 3]

  def move(self, dt, bounds):
    self.x += dt*self.HSPEED
    if(self.x > bounds[0] - 18):
      self.HSPEED = -self.HSPEED
    if(self.x < 18):
      self.HSPEED = -self.HSPEED

  def shot(self):
    pass

# ======== Main ===============

WIDTH = 500
HEIGHT = 350

ship     = Player((250, 300))
ufo      = Alien((20, 30))
ufo.shot = False
missiles = []

# draw() after update() each frame
def draw():
  screen.clear() # is a MUST
  # first draw background
  screen.blit('earth-moon', (0, 0))
  # then draw missiles
  _renderMissiles()
  # last ship on the top of missiles
  ship.draw()
  # one uft
  if not ufo.shot:
    ufo.draw()

def _renderMissiles():
  for missile in missiles: # waiting for missle add
    missile.draw()

def update(dt):
  # move ship horizontally
  ship.move(dt, (WIDTH, HEIGHT))
  # move ship vertically ?
  _updateMissiles()
  # print('missiles length:', len(missiles))
  ufo.update()
  ufo.move(dt, (WIDTH, HEIGHT))
  _hitAlien()


def _updateMissiles():
  for missile in missiles: # update position
    missile.y -= 3
    if(missile.y < 0):
      missiles.remove(missile)

def on_key_down(key):
  global HSPEED, FIRE

  if key == keys.SPACE:
    print('create new missile')
    _fire()

  if key == keys.LEFT :
    ship.toLeft()
    print('move left')

  if key == keys.RIGHT:
    ship.toRight()
    print('move right')

  if key == keys.UP:
    print('move up')

  if key == keys.DOWN:
    print('move down')

def on_key_up(key):
  ship.stopMove()

def on_mouse_move(pos):
  # ship.angle = ship.angle_to(pos)
  pass

def _fire():
  missile = Actor('bomb_s')
  missile.pos = ship.pos[0], ship.pos[1] - 20
  missiles.append(missile)
  sounds.fire.play()

def _hitAlien():
  c = ufo.collidelist(missiles)
  if c > -1:
    ufo.shot = True
