from unicurses import * 

def main():
    
    stdscr = initscr() #start up screen and initalize ncurses

    max_y,max_x=getmaxyx(stdscr)

    move(max_y/2,max_x/2)
    addstr("@ [max colums x= "+str(max_x)+" max rows y= "+str(max_y)+"]")

    getch()
    endwin() #for stop ncurses

    return 0

if(__name__=="__main__"):
    main()