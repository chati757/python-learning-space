from unicurses import * 

def main():
    
    stdscr = initscr() #start up screen and initalize ncurses

    addstr("hello world") #for add string in curses screen 
    getch() #for wait cursor in screeb.press anykey for exit
    #or stop execute anything after that until user get anykey

    endwin() #for stop ncurses

    return 0

if(__name__=="__main__"):
    main()
