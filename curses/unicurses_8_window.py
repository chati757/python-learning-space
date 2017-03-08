from unicurses import * 

def main():
    
    stdscr = initscr() #start up screen and initalize ncurses

    #determate window
    start_color()
    noecho()
    curs_set(False)
    keypad(stdscr,True) 

    window=newwin(10,5,0,0) #newwin(size nline,size ncols,begin position y,begin position x)
    waddstr(window,"helloworld")

    window2=newwin(10,5,20,20)
    waddstr(window2,"helloworld 2")
 
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