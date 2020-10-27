import arcade

# Set winow configurations
window_width = 700
window_height = 500
window_title = "My Game"


# Function to draw on screen

def on_draw(delta_time):
    # Start game engine
    arcade.start_render()

    # drawing the rectangle box
    arcade.draw_rectangle_filled(on_draw.center_x, on_draw.center_y, 50, 50, arcade.color.YELLOW)

    # changing the center coordinates to create animation effect
    on_draw.center_x += on_draw.shift_x * delta_time
    on_draw.center_y += on_draw.shift_y * delta_time

    # if side cross width (right of screen) return back by decreasing x coordinate
    if (on_draw.center_x + 25 > window_width):
        on_draw.shift_x = -100

    # if side cross height(top of screen) return back by decreasing y coordinate
    if (on_draw.center_y + 25 > window_height):
        on_draw.shift_y = -100

    # return box if side touches bottom by increasing x coordinate
    if (on_draw.center_x - 25 < 0):
        on_draw.shift_x = 100

    # return box if side touches left by increasing y coordinate
    if (on_draw.center_y - 25 < 0):
        on_draw.shift_y = 100

    # finishing engine rendering
    arcade.finish_render()


# Setting values of variables specific to on_draw function
#   initial x coordinate of rectangle
on_draw.center_x = 250
#   initial y coordinate of rectangle
on_draw.center_y = 250

# Shifting value of x coordinate on each time on_draw is called
on_draw.shift_x = 50
# Shifting value of y coordinate on each time on_draw is called
on_draw.shift_y = 50

if __name__ == '__main__':
    # Window is created with user defined configurations
    arcade.open_window(window_width, window_height, window_title)
    # Setting window background color
    arcade.set_background_color(arcade.color.RED)
    # Calling function repeatedly to draw rectangle with changes center coordinates to create animation effect
    arcade.schedule(on_draw, 1 / 60)
    # Keep window open until we close by ourself
    arcade.run()
