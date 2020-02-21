import pygame as pg
import os
import time

SCREENRECT = pg.Rect(0, 0, 640, 480)

main_dir = os.path.split(os.path.abspath(__file__))[0]
print(main_dir)

def load_image(file):
    """ loads an image, prepares it for play
    """
    file = os.path.join(main_dir, "images", file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pg.get_error()))
    return surface


pg.init()

# Set the display mode
winstyle = 0  # |FULLSCREEN
bestdepth = pg.display.mode_ok(SCREENRECT.size, winstyle, 32)
screen = pg.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
# screen = pg.display.set_mode((240,180))

surface = load_image("tank_top_64.png")
rotated = pg.transform.rotate(surface, 30)
screen.blit(rotated, (50,50))

pg.display.flip()

running = True
while running:
  print('do something...')
  for event in pg.event.get():
    # only do something if the event is of type QUIT
    if event.type == pg.QUIT:
      # change the value to False, to exit the main loop
      running = False