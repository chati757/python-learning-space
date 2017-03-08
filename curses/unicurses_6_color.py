from unicurses import * 

def main():
    
    stdscr = initscr() #start up screen and initalize ncurses

    start_color()
    
    #use_default_colors() #using default color terminal background 
    init_pair(1,COLOR_RED,COLOR_WHITE) #init_pair(fg,bg) bg=-1 mean..tranparent

    addstr("hello",color_pair(1)+A_REVERSE)
    use_default_colors()
    addstr("hello 2")
    getch()
    endwin() #for stop ncurses

    return 0

if(__name__=="__main__"):
    main()