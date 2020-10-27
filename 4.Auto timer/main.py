import arcade

window_width=200
window_height=250
window_title="Timer"

class Timer(arcade.Window):
    def __init__(self,window_width,window_height,window_title):
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK)
        self.time=100

    def on_draw(self):
        arcade.start_render()
        cal_min=int(self.time//60)
        cal_sec=int(self.time%60)
        time=f"TIME\n\n{cal_min} : {cal_sec}"
        arcade.draw_text(time,320,350,arcade.color.RED,60)

    def update(self,delta_time):
        self.time+=delta_time



if __name__ == '__main__':
    timer=Timer(window_width,window_height,window_title)
    arcade.run()