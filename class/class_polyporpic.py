class Car:
    def __init__(self, name):    
        self.name = name
    #basic ability for Drone
    def drive(self):             
        raise NotImplementedError("Subclass must implement abstract method")
 
    def stop(self):             
        raise NotImplementedError("Subclass must implement abstract method")
 
class Sportscar(Car):
    def drive(self):
        return 'Sportscar driving!'
 
    def stop(self):
        return 'Sportscar breaking!'
 
class Truck(Car):
    def drive(self):
        return 'Truck driving slowly because heavily loaded.'
 
    def stop(self):
        return 'Truck breaking!'

class Tank(Car):
    def drive(self):
        return 'Tank driving slowly'
    def shoot(self):
        return 'Tank shooting'
 
cars = [Truck('Bananatruck'),
        Truck('Orangetruck'),
        Sportscar('Z3'),
        Tank('t-34')]
 
for car in cars:
    print car.name + ': ' + car.drive()

print(Tank('t-34').shoot())
