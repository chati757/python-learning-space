import time
while 1:
    try:
        time.sleep(5)
        print("in try")
    # and except it when Ctrl + C like happens
    except KeyboardInterrupt:
        print "Ctrl C or alike is pressed..."
        break