from unicurses import * 

def main():
    
    stdscr = initscr() #start up screen and initalize ncurses

    start_color()
    noecho()#not show txt when typing
    curs_set(False)#not show cursor
    keypad(stdscr,True)#register arrow key

    running = True
    
    while(running):
        key = getch()
        if (key==27):
            running = False
            break

if(__name__=="__main__"):
    main()