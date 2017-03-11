from unicurses import * 

def main():
    
    stdscr = initscr() #start up screen and initalize ncurses

    #determate window
    start_color()
    noecho()#not show txt when typing
    curs_set(False)#not show cursor
    keypad(stdscr,True)#register arrow key

    
    window=newwin(3,20,5,5)
    box(window)
    wmove(window,1,1)
    waddstr(window,"window1")

    window2=newwin(3,20,4,4)
    box(window2)
    wmove(window2,1,1)
    waddstr(window2,"window2")

    #panel is container of window

    panel = new_panel(window)#for create panel and specify window
    panel2 = new_panel(window2)

    #move_panel(panel,10,30)
    top_panel(panel)
    
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