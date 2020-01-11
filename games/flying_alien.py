# @2019/12/15

WIDTH = 512
HEIGHT = 410
COUNTER = 0

alien = Actor('alien')
alien.pos = 30, 100
alien.speed = 2

def draw():
    screen.clear()
    screen.blit('earth-moon', (10, 10))
    alien.draw()

def update():
    global COUNTER
    COUNTER += 1
    
    switch = int(COUNTER/10)%2

    if switch > 0 :
      alien.image = 'alien_hurt'
    else:
      alien.image = 'alien'

    # current position
    alien.left += alien.speed
    # if alien move beyond right
    if alien.left > WIDTH - 66:
        # speed decrease
        alien.speed = -2
    if alien.left < 0:
      alien.speed = 2