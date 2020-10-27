import arcade

window_width=800
window_height=600
window_title="Moving rectangle using Arcade"

rectangle_width=80
rectangle_height=60

initial_x=100
initial_y=200

rectangle_speed=5

class Rectangle():
    def __init__(self,width,height,color):
        self.center_x=initial_x
        self.center_y=initial_y
        self.color=color
        self.width=width
        self.height=height
        self.new_x=0
        self.new_y=0


    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)

    def move(self):
        self.center_x+=self.new_x
        self.center_y+=self.new_y

        if self.center_x <rectangle_width//2:
            self.center_x=rectangle_width//2
        elif self.center_x>window_width-rectangle_width//2:
            self.center_x=window_width-rectangle_width//2

        if self.center_y < rectangle_height // 2:
            self.center_y = rectangle_height // 2
        elif self.center_y > window_height - rectangle_height // 2:
            self.center_y = window_height - rectangle_height // 2


class Game(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.box = Rectangle( rectangle_width, rectangle_height, arcade.color.RED)

    def on_draw(self):
        arcade.start_render()
        self.box.draw()

    def update(self,dt):
        self.box.move()

    def on_key_press(self, key):
        if key==arcade.key.UP:
            self.box.new_y=rectangle_speed
        if key == arcade.key.DOWN:
            self.box.new_y = -rectangle_speed
        if key == arcade.key.LEFT:
            self.box.new_x = -rectangle_speed
        if key == arcade.key.RIGHT:
            self.box.new_y = rectangle_speed
    def on_key_release(self, key):
        if key==arcade.key.UP or key==arcade.key.DOWN:
            self.box.new_y=0
        else:
            self.box.new_x=0

if __name__ == '__main__':
    obj=Game(window_width,window_height,window_title)
    arcade.run()