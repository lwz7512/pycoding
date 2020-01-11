# first Pygame-zero project
# @2020/01/08

# from pygame import Surface, Rect
# from pygame.constants import HWSURFACE, SRCALPHA


WIDTH = 500
HEIGHT = 350

SPEED = 0

# init actors first
ship     = Actor('ship_s')
ship.pos = 250, 300
# missile     = Actor('bomb_s')
missiles = []



# draw() after update() each frame
def draw():
  screen.clear() # is a MUST
  screen.blit('earth-moon', (0, 0))
  ship.draw()
  
  for missile in missiles: # waiting for missle add
    missile.draw()


def update(dt):
  ship.x += SPEED
  # print('update...')
  for missile in missiles: # update position
    missile.y -= 3
    if(missile.y < 0):
      missiles.remove(missile)
  
  print('missiles length:', len(missiles))


def on_key_down(key):
  global SPEED, FIRE

  if key == keys.SPACE:
    print('create new missile')
    missile = Actor('bomb_s')
    missile.pos = ship.pos[0], ship.pos[1] - 20
    missiles.append(missile)
    sounds.fire.play()

  if key == keys.LEFT:
    SPEED = -4
    print('move left')

  if key == keys.RIGHT:
    SPEED = 4
    print('move right')

  if key == keys.UP:
    print('move up')

  if key == keys.DOWN:
    print('move down')


def on_key_up(key):
  global SPEED

  SPEED = 0

def on_mouse_move(pos):
  # ship.angle = ship.angle_to(pos)
  pass