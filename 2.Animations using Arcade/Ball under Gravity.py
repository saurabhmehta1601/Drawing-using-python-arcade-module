import arcade

window_width = 700
window_height = 500
window_title = "My Game"

def draw(delta_time):
    arcade.start_render()
    draw.width=window_width
    arcade.draw_circle_filled(draw.center_x,draw.center_y,20,arcade.color.LEMON_CURRY)

    draw.center_x+=draw.shift_x
    draw.center_y+=draw.shift_y

    if(draw.center_y+20>draw.height):
        draw.shift_y*=-1
        draw.height-=draw.gravity
    if (draw.center_y - 20 < 0):
        draw.shift_y *= -1
        draw.height-=draw.gravity

    arcade.finish_render()

draw.center_x=100
draw.center_y=200
draw.height = 400

draw.shift_x=1
draw.shift_y=6

draw.bounciness=1
draw.gravity=0.2


if __name__ == '__main__':
    arcade.open_window(window_width,window_height,window_title)
    arcade.set_background_color(arcade.color.AMAZON)
    arcade.schedule(draw,1/60)
    arcade.run()