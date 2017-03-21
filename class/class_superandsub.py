class drone_prototype:
    def __init__(self, name):    
        self.name = name
    #basic ability for Drone
    def trackline(self):             
        return "trackline.."
    def move(self):             
        return "move.."
    def stop(self):             
        return "stop.."
    def turn_back(self):
        return "turn back.."
    def turn_left(self):
        return "turn left.."
    def turn_right(self):
        return "turn right.."

class water_drone(drone_prototype):
    def pump(self):
        return "pump.."

wd=water_drone("wd1")
print(wd.trackline())
print(wd.pump())
