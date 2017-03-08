from unicurses import * 

def main():
    
    stdscr = initscr() #start up screen and initalize ncurses

    attron(A_REVERSE) #attribute on bold and blink and ...
    addstr("hello world\n")
    attroff(A_REVERSE)
    
    addstr("hello world",A_REVERSE)

    getch()
    endwin() #for stop ncurses

    return 0

if(__name__=="__main__"):
    main()