from unicurses import * 

def main():
    
    stdscr = initscr() #start up screen and initalize ncurses

    start_color()
    use_default_colors()
    #use_default_colors() #using default color terminal background 
    init_pair(1,COLOR_RED,COLOR_WHITE) #init_pair(fg,bg) bg=-1 mean..tranparent

    addstr("hello 1",color_pair(1)+A_REVERSE)

    init_pair(2,14,-1) #init_pair(fg,bg) bg=-1 mean..tranparent
    
    addstr("hello 2",color_pair(2))

    init_pair(3,11,-1) #init_pair(fg,bg) bg=-1 mean..tranparent
    
    addstr("hello 3",color_pair(3))

    addstr("hello 4")
    getch()
    endwin() #for stop ncurses

    return 0

if(__name__=="__main__"):
    main()