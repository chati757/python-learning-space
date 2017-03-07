from unicurses import * 

def main():
    
    stdscr = initscr() #start up screen and initalize ncurses

    move(5,30) # move(y,x) row,colum not x,y
    addstr("hello world") #for add string in curses screen
    #or your can use
    #mvaddstr("hello world")
    '''
    for i in range(0,50):
        mvaddstr(10,i,"hello")
        getch()
    '''
    getch() #for wait cursor in screeb.press anykey for exit
    #or stop execute anything after that until user get anykey

    endwin() #for stop ncurses

    return 0

if(__name__=="__main__"):
    main()
