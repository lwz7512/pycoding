# moving tank
# @2020/01/27

import math
from pygame.math import Vector2

# =================== MAIN ================================
WIDTH  = 300
HEIGHT = 400

ROTATION_SPEED = 0
bullets = []
# MAX_DISTANCE = min(WIDTH, HEIGHT) * .95

tank = {
  "top" : Actor('tank_top_64'),
  "base": Actor('tank_base_64'),
  "pos" : (150, 360)
}

def update(dt):
  tank['top'].angle += ROTATION_SPEED
  for bullet in bullets:
    bullet.exact_pos = bullet.exact_pos - (bullet.velocity * dt)
    bullet.pos = bullet.exact_pos.x % WIDTH, bullet.exact_pos.y % HEIGHT
    if bullet.x < 10 or bullet.x > 290 or bullet.y < 10 :
      bullets.remove(bullet)

def draw():
  screen.fill('black')
  for bullet in bullets:
    bullet.draw()
  tank['base'].pos = tank['pos']
  tank['base'].draw()
  tank['top'].pos = tank['pos'][0], tank['pos'][1] + 4
  tank['top'].draw()

def on_key_down(key):
  if key == keys.SPACE:
    bullets.append(_fire(tank['top']))
    sounds.fire.play()
  if key == keys.LEFT :
    _turnLeft()
  if key == keys.RIGHT:
    _turnRight()
  if key == keys.UP:
    pass
  if key == keys.DOWN:
    pass

def on_key_up(key):
  global ROTATION_SPEED
  ROTATION_SPEED = 0

def _turnLeft():
  global ROTATION_SPEED
  ROTATION_SPEED = 1

def _turnRight():
  global ROTATION_SPEED
  ROTATION_SPEED = -1

def _fire(gun):
  bullet = Actor('bullet', pos=(150, 360))
  ang = math.radians(gun.angle)
  bullet.angle = gun.angle
  bullet.exact_pos = bullet.start_pos = Vector2(gun.pos)
  bullet.velocity = Vector2(math.sin(ang), math.cos(ang)).normalize() * 400.0
  return bullet
