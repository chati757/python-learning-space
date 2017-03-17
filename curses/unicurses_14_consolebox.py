from unicurses import * 

#ref = http://stackoverflow.com/questions/21784625/how-to-input-a-word-in-ncurses-screen
def main():
    
    stdscr = initscr() #start up screen and initalize ncurses
    echo() 
    curs_set(True)#not show cursor
    keypad(stdscr,True)#register arrow key

    window = newwin(30,30,0,0)
    box(window)

    #clear()
    choice = my_raw_input(stdscr,window, 2, 3, "cool or hot?").lower()
    if choice == "cool":
        mvwaddstr(window,5,3,"Super cool!") #mvaddstr(5,3,"Super cool!")
    elif choice == "hot":
        mvwaddstr(window,5,3,"HOT") #mvaddstr(5,3," HOT!") 
    else:
        mvwaddstr(window,5,3,"Invalid input") #mvaddstr(5,3," Invalid input") 

    running = True
    while(running):
        key=wgetch(window)#don't forget setting window2 or window in this line
        if(key==27):
            running = False
            break

    endwin() #for stop ncurses

    return 0

def my_raw_input(stdscr,window,r,c, prompt_string):
    mvwaddstr(window,r,c,prompt_string) #mvaddstr(r, c, prompt_string)
    refresh()
    input = mvgetstr(r + 1,c)
    return input

def quest():


if(__name__=="__main__"):
    main()
