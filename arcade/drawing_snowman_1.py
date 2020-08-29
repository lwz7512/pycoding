import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()

# Draw the ground
arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

# Draw a snow person

# Snow
arcade.draw_circle_filled(400, 200, 80, arcade.color.WHITE)
arcade.draw_circle_filled(400, 280, 50, arcade.color.WHITE)
arcade.draw_circle_filled(400, 340, 40, arcade.color.WHITE)

# Eyes
arcade.draw_circle_filled(385, 350, 5, arcade.color.BLACK)
arcade.draw_circle_filled(415, 350, 5, arcade.color.BLACK)
arcade.draw_circle_filled(400, 330, 5, arcade.color.BLACK)

# Moon
arcade.draw_circle_filled(200, 500, 50, arcade.color.WHITE)
arcade.draw_circle_filled(180, 510, 40, arcade.color.BLACK)

#  Finish and run
arcade.finish_render()
arcade.run()