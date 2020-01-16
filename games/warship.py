# first Pygame-zero project
# @2020/01/08

# from pygame import Surface, Rect
# from pygame.constants import HWSURFACE, SRCALPHA


# ======== Alien UFO ==========
class Alien(Actor):

  animcycle = 9
  HSPEED = 90

  def __init__(self, startpoint, **kwargs):
    super(Alien, self).__init__('alien1', **kwargs)
    self.frame = 0
    self.stp = startpoint
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
HSPEED = 0

# init actors first
ship     = Actor('ship_s')
ship.pos = 250, 300
# missile  = Actor('bomb_s')
missiles = []
ufo      = Alien((20, 30))


# draw() after update() each frame
def draw():
  screen.clear() # is a MUST
  # first draw background
  screen.blit('earth-moon', (0, 0))
  # then draw missiles
  for missile in missiles: # waiting for missle add
    missile.draw()
  # last ship on the top of missiles
  ship.draw()
  # one uft
  ufo.draw()


def update(dt):
  print('ship x:', ship.x)
  # move ship horizontally
  # if ship.pos[0] >= 30 and ship.pos[0] <= WIDTH-30:
  if ship.x + HSPEED > 30 and ship.x + HSPEED < WIDTH-30:
    ship.x += HSPEED
  # move ship vertically ?
  
  # print('update...')
  for missile in missiles: # update position
    missile.y -= 3
    if(missile.y < 0):
      missiles.remove(missile)
  
  # print('missiles length:', len(missiles))
  ufo.update()
  ufo.move(dt, (WIDTH, HEIGHT))


def on_key_down(key):
  global HSPEED, FIRE

  if key == keys.SPACE:
    print('create new missile')
    missile = Actor('bomb_s')
    missile.pos = ship.pos[0], ship.pos[1] - 20
    missiles.append(missile)
    sounds.fire.play()

  if key == keys.LEFT :
    HSPEED = -4
    print('move left')

  if key == keys.RIGHT:
    HSPEED = 4
    print('move right')

  if key == keys.UP:
    print('move up')

  if key == keys.DOWN:
    print('move down')


def on_key_up(key):
  global HSPEED
  HSPEED = 0
  if ship.pos[0] < 30:
    ship.x = 30
  if ship.pos[0] > WIDTH-30:
    ship.x = WIDTH-30

def on_mouse_move(pos):
  # ship.angle = ship.angle_to(pos)
  pass