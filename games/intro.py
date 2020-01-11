WIDTH = 500
HEIGHT = 200

alien = Actor('alien')
alien.pos = 30, 100
alien.speed = 2

def draw():
    screen.clear()
    alien.draw()

def update():
    # current position
    alien.left += alien.speed
    # if alien move beyond right
    if alien.left > WIDTH - 66:
        # speed decrease
        alien.speed = -2
    if alien.left < 0:
      alien.speed = 2