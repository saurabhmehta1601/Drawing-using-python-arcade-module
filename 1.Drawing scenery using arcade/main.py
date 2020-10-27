import arcade
# Initializing dimensions and title of screen
window_width=700
window_height=500
window_title="Arcade "

# Setting the background of screen

def set_background():
    arcade.draw_lrtb_rectangle_filled(0,window_width,window_height*(1/3),0,arcade.color.DARK_SPRING_GREEN)
    arcade.draw_lrtb_rectangle_filled(0,window_width,window_height,window_height*(1/3),arcade.color.SKY_BLUE)

# Creating tree

def draw_tree(x,y):

    arcade.draw_triangle_filled(x-50,y,x+50,y,x,y+100,arcade.color.MSU_GREEN)
    arcade.draw_lrtb_rectangle_filled(x-25,x+25,y,y-70,arcade.color.BROWN)

# Creating trees using tree function

def draw_trees():
    for x in range (50,700,100):
        draw_tree(x,190)

# Creating birds with custom positions and scale(make them look closer or far)

def draw_bird(x,y,scale):
    arcade.draw_arc_outline(x,y,40*scale,30*scale,arcade.color.BLACK,0,90,3*scale)
    arcade.draw_arc_outline(x+40*scale,y,40*scale,30*scale,arcade.color.BLACK,90,180,2.25*scale)

# Creating random birds by using draw_bird function

def draw_birds():
    draw_bird(200, 400, 0.9)
    draw_bird(300, 300, 1.2)
    draw_bird(30, 450, 0.8)
    draw_bird(70, 350, 0.6)
    draw_bird(650, 350, 0.6)
    draw_bird(500, 340, 0.9)

# Opening window using arcade

arcade.open_window(window_width,window_height,window_title)

# Intializing arcade engine
arcade.start_render()

set_background()
draw_birds()
draw_trees()




arcade.finish_render()
# Engine rendering is finished

# Keep winodw open until user close window
arcade.run()