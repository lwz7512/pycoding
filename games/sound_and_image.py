# WIDTH = 300
# HEIGHT = 300

# def draw():
#     screen.fill((128, 0, 0))

alien = Actor('alien')
alien.pos = 100, 56
# alien.topright = 0, 10

WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()
    alien.draw()

def update():
  pass

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        sounds.eep.play()
        alien.image = 'alien_hurt'
    else:
      print('not collide!')
      alien.image = 'alien'