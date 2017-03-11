from unicurses import * 

def main():
    
    stdscr = initscr() #start up screen and initalize ncurses

    #determate window
    start_color()
    noecho()#not show txt when typing
    curs_set(False)#not show cursor
    keypad(stdscr,True)#register arrow key 

    window=newwin(10,25,3,3) #newwin(size nline,size ncols,begin position y,begin position x)
    box(window)
    waddstr(window,"helloworld")

    window2=newwin(10,25,3,3) #newwin(size nline,size ncols,begin position y,begin position x)
    box(window2)
    wmove(window2,1,1)
    waddstr(window2,"helloworld1")
 
    running = True
    while(running):
        key=wgetch(window2)#don't forget setting window2 or window in this line
        if(key==27):
            running = False
            break

    endwin() #for stop ncurses

    return 0

if(__name__=="__main__"):
    main()