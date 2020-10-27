import arcade
# moving ball using OOP

class MovingBall(arcade.Window):
    def __init__(self,width,height,title):
        # calling constructor of parent class of MovingBall class i.e arcade.Window
        super().__init__(width,height,title)
        # Setting window background
        arcade.set_background_color(arcade.color.GOLD)
        # Setting class variables
        self.width=width
        self.height=height
        self.center_x=100
        self.center_y=200
        self.shift_x=1
        self.shift_y=4
        self.radius=40

    # Gets automatically called 60 times in every second drawing circle with updated coordinates
    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.center_x,self.center_y,self.radius,arcade.color.RED)
    # Gets called every 1/60 part of second updates coordinates of circle
    def on_update(self, delta_time):
        self.center_x+=self.shift_x
        self.center_y+=self.shift_y
        # if cicles gets out of window revert back

        # if center coordinate value gets more and can't fit in window decrease them by adding negative shifting
        if(self.center_x+self.radius>=self.width):
            self.shift_x *= -1
        if (self.center_y + self.radius >= self.height):
            self.shift_y *= -1
        #     if center coordinate value gets less and can't fit in window increase by adding positive shifting
        if (self.center_x - self.radius <= 0):
            self.shift_x *= -1
        if (self.center_y - self.radius <= 0):
            self.shift_y *= -1


if __name__ == '__main__':
    MovingBall(700,500,"Moving Ball")
    arcade.run()