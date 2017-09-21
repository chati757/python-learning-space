import time
class RaspberryThread(threading.Thread):
    def __init__(self, function):
        self.running = False
        self.function = function
        super(RaspberryThread, self).__init__()

    def start(self):
        self.running = True
        super(RaspberryThread, self).start()

    def run(self):
        while self.running:
            self.function()

    def stop(self):
        self.running = False

v1 = RaspberryThread(function = shoppingcart)
v2 = RaspberryThread(function = dodgeballs)

v1.start()
v2.start()

time.sleep(10)

v1.stop()
v2.stop()