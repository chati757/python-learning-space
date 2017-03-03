def OnKeyboardEvent(event):
    #do something
    print ("do something",event)
    return True

class hooks_manager:
    print("in class")

    def __init__(self):
        print("in init")
        #receive external variable for use in class
        #self.fncb=fncb
        #allow function for external call
        self.keydown()

    def keydown(self):
        print("inclass functin keydown")

    '''
    def run(self):
        print("in run")
        self.keydown("some event")
    '''
if __name__=="__main__":
    print("in main")
    hm = hooks_manager()
    hm.keydown=OnKeyboardEvent
    print(hm.keydown)