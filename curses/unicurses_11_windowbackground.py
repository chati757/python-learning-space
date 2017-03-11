from unicurses import * 

def main():
    
    stdscr = initscr() #start up screen and initalize ncurses

    #determate window
    start_color()
    use_default_colors()
    noecho()#not show txt when typing
    curs_set(False)#not show cursor
    keypad(stdscr,True)#register arrow key

    #color initalize
    init_pair(1,COLOR_YELLOW,COLOR_GREEN)
    init_pair(2,COLOR_RED,COLOR_GREEN)
    #init_pair(2,COLOR_RED,-1)

    #window initalize background ex
    dude = newwin(1,1,10,30)
    box(dude)
    waddstr(dude,"@",color_pair(2))

    grass = newwin(10,50,5,5)
    box(grass)
    wbkgd(grass,color_pair(1))
    #wbkgd(grass,1,color_pair(1))

    #panel initalize
    dude_panel = new_panel(dude)
    grass_panel = new_panel(grass)

    #set default position panel
    bottom_panel(grass_panel)

    update_panels()
    doupdate()
    

    running = True
    while(running):
        key=getch()#don't forget setting window2 or window in this line
        if(key==27):
            running = False
            break

    endwin() #for stop ncurses

    return 0

if(__name__=="__main__"):
    main()