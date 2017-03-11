from unicurses import * 

global_color_number = 1
def make_color(fg,bg):

    global global_color_number

    color_number = global_color_number
    init_pair(color_number,fg,bg)

    global_color_number +=1

    return color_number

# this function can be import and replace to init_pair
# ex using in another file 
# import <thisfilename> import *
# red = make_color(COLOR_RED,COLOR_BLACK)
# print(red) < #color number can be represent this