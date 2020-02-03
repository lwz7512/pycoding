# moving tank
# @2020/01/27

# =================== MAIN ================================
WIDTH  = 300
HEIGHT = 400

ROTATION_SPEED = 0

tank = {
  "top" : Actor('tank_top_64'),
  "base": Actor('tank_base_64'),
  "pos" : (150, 360)
}

def update(dt):
  tank['top'].angle += ROTATION_SPEED

def draw():
  screen.fill('white')
  tank['base'].pos = tank['pos']
  tank['base'].draw()
  tank['top'].pos = tank['pos'][0], tank['pos'][1] + 4
  tank['top'].draw()

def on_key_down(key):
  if key == keys.SPACE:
    pass
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
