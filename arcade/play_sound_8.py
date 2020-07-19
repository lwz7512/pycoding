import arcade
import os

arcade.open_window(300, 300, "Sound Demo")

soundPath = os.path.join('arcade', 'laser.ogg')
laser_sound = arcade.load_sound(soundPath)

arcade.play_sound(laser_sound)
arcade.run()