from unicurses import * 

#ref = http://stackoverflow.com/questions/21784625/how-to-input-a-word-in-ncurses-screen
def main():
    
    stdscr = initscr() #start up screen and initalize ncurses
    echo() 
    curs_set(True)#not show cursor
    keypad(stdscr,True)#register arrow key

    window = newwin(30,30,0,0)
    box(window)
    panel = new_panel(window)

    #clear()
    choice = my_raw_input(stdscr,window, 2, 3, "cool or hot?").lower()
    if choice == "cool":
        mvwaddstr(window,5,3,"Super cool!") #mvaddstr(5,3,"Super cool!")
    elif choice == "hot":
        mvwaddstr(window,5,3,"HOT") #mvaddstr(5,3," HOT!") 
    else:
        mvwaddstr(window,5,3,"Invalid input") #mvaddstr(5,3," Invalid input") 
        
    box(window)
    update_panels()
    doupdate()
    endwin() #for stop ncurses

  

def my_raw_input(stdscr,window,row,col, prompt_string):
    #display cool or hot?
    mvwaddstr(window,row,col,prompt_string) #mvaddstr(r, c, prompt_string)
    #refresh() #return to line 1 again
    input = mvwgetstr(window,(row + 1),col) #wait input for this line
    return input

if(__name__=="__main__"):
    main()
