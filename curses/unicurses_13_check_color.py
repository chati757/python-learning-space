from unicurses import * 

stdscr = initscr()

def main():
    start_color()
    use_default_colors()
    for i in range(0,255):
        init_pair(i + 1, i, -1)
    try:
        for i in range(0, 255):
            addstr(str(i),color_pair(i))
    except:
        # End of screen reached
        pass
    getch()

if(__name__=="__main__"):
    main()