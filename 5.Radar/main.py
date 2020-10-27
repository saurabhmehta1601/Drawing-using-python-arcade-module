import arcade
import math

window_width=700
window_height=500
window_title="Radar"


class Radar(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.BLACK)
        self.center_x=window_width//2
        self.center_y=window_height//2
        self.radius=200
        self.angle=0

        self.thickness=5
    def on_draw(self):
        arcade.start_render()
        self.end_x = self.center_x + self.radius * math.cos(self.angle)
        self.end_y = self.center_y + self.radius * math.sin(self.angle)
        arcade.draw_circle_outline(self.center_x,self.center_y,self.radius,arcade.color.BLUE,self.thickness)
        arcade.draw_line(self.center_x,self.center_y,self.end_x,self.end_y,arcade.color.RED,self.thickness)

    def update(self,new_time):
        self.angle-=0.02

if __name__ == '__main__':
    radar=Radar(window_width,window_height,window_title)
    arcade.run()