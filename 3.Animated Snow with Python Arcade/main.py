# import required modules
import arcade
import math
import random

# Our window screen configurations
window_width=800
window_height=600
window_title="Snowfall"

# Defining Snowflake for snowfall
class Snow:
    def __init__(self):
        # Initial snow flake postition
        self.x=0
        self.y=0
    # Reseting the postition
    def reset_position(self):
        self.x=random.randrange(window_width)
        self.y=random.randrange(window_height,window_height+400)
    #Define  functions for creating snowfall animations
class Snowfall(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.BLACK)

        # Creating snowflake and its properties

    def start_snowfall(self):
        # Create list of snowflakes
        self.snowflakes_list = []
        #  choose no of snowflakes to create
        for i in range(100):
            snowflake = Snow()
            # Snowflake properties
            snowflake.x=random.randrange(window_width)
            snowflake.y=random.randrange(window_height+100)
            snowflake.size = random.randrange(3)
            snowflake.angle=random.uniform(math.pi,2*math.pi)
            snowflake.speed = random.randrange(20, 100)
            self.snowflakes_list.append(snowflake)
    # These two method are Automatically triggered when instance of this call is created
    # Draws on window
    def on_draw(self):
        arcade.start_render()
        for snowflake in self.snowflakes_list:
            arcade.draw_circle_filled(snowflake.x,snowflake.y,snowflake.size,arcade.color.WHITE_SMOKE)

    # updates location of snowflake
    def update(self,delta_time):
        for snowflake in self.snowflakes_list:
            snowflake.y-=delta_time*snowflake.speed
            snowflake.x+=snowflake.speed*delta_time* math.cos(snowflake.angle)
            snowflake.angle+=1*delta_time
            if snowflake.y<0:
                snowflake.reset_position()

if __name__ == '__main__':
    snow=Snowfall(window_width,window_height,window_title)
    snow.start_snowfall()
    arcade.run()