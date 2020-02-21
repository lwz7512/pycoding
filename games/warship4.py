# warship step 3: Multiple UFO with explostion effect
# @2020/02/15

import random

# ======== Player =============
class Player(Actor):

  HSPEED = 0

  def __init__(self, startpoint, **kwargs):
    super(Player, self).__init__('ship2', **kwargs)
    self.frame = 0
    self.pos = startpoint
    self.alive = True

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

  def __init__(self, startpoint, bounds, **kwargs):
    super(Alien, self).__init__('alien1', **kwargs)
    self.frame = 0
    self.start = startpoint # remember the init position
    self.pos = startpoint
    self.bounds = bounds
    self.images = ['alien1', 'alien2', 'alien3']
    self.HSPEED = random.choice([-1, 1])*90
    self.shot = False
    self.bomb = Actor('bomb2')
    self.bomb.pos = startpoint

  def blink(self):
    # change skin
    self.frame = self.frame + 1
    self.image = self.images[self.frame // self.animcycle % 3]

  def move(self, dt, bounds):
    self.x += dt*self.HSPEED
    if(self.x > bounds[0] - 18):
      self.HSPEED = -self.HSPEED
    if(self.x < 18):
      self.HSPEED = -self.HSPEED

  def update(self):
    self.bomb.pos = self.start[0], self.bomb.pos[1]+3

  def draw(self):
    super(Alien, self).draw()
    if(self.bomb.y < self.bounds[0]-150):
      self.bomb.draw()

# ============ EXPLOSION =========
class Explosion(Actor):

  animcycle = 6
  loop = 3

  def __init__(self, startpoint, **kwargs):
    super(Explosion, self).__init__('explosion1', **kwargs)
    self.show = False
    self.complete = False
    self.frame = 0
    self.pos = startpoint
    self.images = ['explosion1', 'explosion2', 'explosion3']
  
  def display(self, pos):
    self.pos = pos
    self.show = True
    self.frame = 0
    self.complete = False

  def blink(self):
    if not self.show:
      return
    # change skin
    self.frame = self.frame + 1
    self.image = self.images[self.frame // self.animcycle % 3]
    if self.frame >= self.animcycle * self.loop:
      self.complete = True

  def draw(self):
    if self.show and not self.complete:
      super(Explosion, self).draw()



# ============ MAIN ===============

WIDTH = 500
HEIGHT = 350

ship        = Player((250, 300))
missiles    = []
ufoHomeShip = []
shoted      = 0
explosion   = Explosion((0, 0))

def _createAlien():
  # print('create one alien...')
  rnd = random.randint(40, 400)
  ufo = Alien((rnd, 50), (WIDTH, HEIGHT))
  if len(ufoHomeShip) < 10:
    ufoHomeShip.append(ufo)

# draw() after update() each frame
def draw():
  screen.clear() # is a MUST
  # first draw background
  screen.blit('earth-moon', (0, 0))
  # draw score:
  screen.draw.text("YOU SHOT "+str(shoted)+" UFO", (10, 10), color="blue")
  # last ship on the top of missiles
  if ship.alive:
    ship.draw()
  # draw ufos
  for ufo in ufoHomeShip:
    ufo.draw()
  # then draw missiles
  _renderMissiles()
  if not explosion.complete:
    explosion.draw()
  # game over
  if not ship.alive:
    screen.draw.text("GAME OVER", (120, 150), color="red", fontsize=60, owidth=1, ocolor="orange")

def _renderMissiles():
  for missile in missiles: # waiting for missle add
    missile.draw()

def update(dt):
  # move ship horizontally
  ship.move(dt, (WIDTH, HEIGHT))
  # move ship vertically ?
  _updateMissiles()
  _updateUFOs(dt)
  _hitAlien()
  _hitShip()
  explosion.blink()  

def _updateUFOs(dt):
  for ufo in ufoHomeShip:
    ufo.blink()
    ufo.move(dt, (WIDTH, HEIGHT))
    ufo.update()

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
  pass

def _fire():
  missile = Actor('bomb_s')
  missile.pos = ship.pos[0], ship.pos[1] - 20
  missiles.append(missile)
  sounds.fire.play()

def _hitAlien():
  global shoted
  for ufo in ufoHomeShip:
    for missile in missiles:
      shot = ufo.collidepoint(missile.center)
      if shot:
        ufo.shot = True # remember the ufo being shoted
        return missiles.remove(missile)
  for ufo in ufoHomeShip:
    if ufo.shot:
      shoted += 1
      explosion.display(ufo.center)
      sounds.boom.play()
      return ufoHomeShip.remove(ufo)

def _hitShip():
  for ufo in ufoHomeShip:
    if ship.colliderect(ufo.bomb) and ship.alive:
      ship.alive = False
      explosion.display(ship.center)
      sounds.boom.play()
      return

_createAlien()
clock.schedule_interval(_createAlien, 2)