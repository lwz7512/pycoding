import arcade

class MyApplication(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height, "Trigger Sound With Key")

        # Load the sound when the application starts
        self.laser_sound = arcade.load_sound(":resources:sounds/coin1.wav")

    def on_draw(self):
        arcade.start_render()
        
        start_x = 50
        start_y = 150
        arcade.draw_text("Press space key to play sound", start_x, start_y, arcade.color.WHITE, 12)

    
    def on_key_press(self, key, modifiers):

        # If the user hits  the space bar, play the sound that we loaded
        if key == arcade.key.SPACE:
            arcade.play_sound(self.laser_sound)


def main():
    window = MyApplication(300, 300)
    arcade.run()

main()