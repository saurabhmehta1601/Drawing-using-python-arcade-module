import arcade
# Setting window dimensions and title
window_width=800
window_height=600
window_title="My moving rectangle"

# rectangle properties
rectangle_width=80
rectangle_height=60
rectangle_color=arcade.color.BLUE
rectangle_speed=10
# Initial rectangle position
rectangle_initial_x=100
rectangle_initial_y=100

# Defining rectangle class
class Rectangle():
    def __init__(self,x,y,width,height,color):
        self.center_x=x
        self.center_y=y
        self.width=width
        self.height=height
        self.color=color
        self.shift_x=0
        self.shift_y=0
    # Draws rectangle
    def draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)
    # Changes center coordinates
    def move(self):
        self.center_x+=self.shift_x
        self.center_y+=self.shift_y
        # If rectangle goes out of window push back by reseting its center coordinates
        if self.center_x<rectangle_width//2 :
            self.center_x=rectangle_width//2
        elif self.center_x > window_width-rectangle_width//2 :
            self.center_x = window_width - rectangle_width // 2

        if self.center_y<rectangle_height//2 :
            self.center_y=rectangle_height//2
        elif self.center_y > window_height - rectangle_height // 2:
            self.center_y = window_height - rectangle_height // 2


class Game(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.BLACK)
        self.box=Rectangle(rectangle_initial_x,rectangle_initial_y,rectangle_width,rectangle_height,rectangle_color)

    # These Functions are called automatically continuously as soon as object of this class is created
    # Draws rectangle continuously with changes coordinates creating animation effect
    def on_draw(self):
        self.box.draw()
    def update(self, delta_time):
        self.box.move()
    # Changes center coordinates of rectangle based on which key is pressed i.e LEFT,RIGHT,UP and DOWN
    def on_key_press(self, key, modifiers):
        if key==arcade.key.UP:
            self.box.shift_y=rectangle_speed
        if key==arcade.key.DOWN:
            self.box.shift_y=-rectangle_speed
        if key == arcade.key.LEFT:
            self.box.shift_x = -rectangle_speed
        if key == arcade.key.RIGHT:
            self.box.shift_x = rectangle_speed

    # Setting change values in coordinates to zero with key release so that speed does't change each time key is pressed
    def on_key_release(self, key, modifiers):
        if key==arcade.key.UP or key==arcade.key.DOWN:
            self.box.shift_x=0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.box.shift_x = 0

# Main method
if __name__ == '__main__':
    myGame=Game(window_width,window_height,window_title)
    arcade.run()