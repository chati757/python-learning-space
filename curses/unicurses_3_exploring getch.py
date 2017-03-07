from unicurses import * 

def main():
    
    stdscr = initscr() #start up screen and initalize ncurses

    running = True
    while(running):
        key = getch()
        if (key == 27):#27 mean escape button
            running = False
            break
        elif(chr(key)=="a"):
            move(2,0)
            addstr("pressed a and > ord a is "+str(ord('a')))
            move(0,0)
            continue
        elif(key==ord('b')):
            move(3,0)
            addstr("pressed b and > ord a is "+str(ord('b')))
            move(0,0)
            continue
        move(10,0)
        addstr("Keycode was "+str(key)+" and the key was "+ chr(key)) 
        #chr() for convert ascii to charactor 
        move(0,0)

    endwin() #for stop ncurses

    return 0

if(__name__=="__main__"):
    main()