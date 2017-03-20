#Preventing direct creation type
import random

'''
#prevent type one 
class Shape(object):
    types = [] #old shapeNameGen variable.
    create types = [] becase easy to change to not prevent mode

def factory(type):
    class Circle(Shape):
        def draw(self): print("Circle.draw")
        def erase(self): print("Circle.erase")

    class Square(Shape):
        def draw(self): print("Square.draw")
        def erase(self): print("Square.erase")

    if type == "Circle": return Circle()
    if type == "Square": return Square()
    assert 0, "Bad shape creation: " + type
    #and change in shapeNameGen function
    #provide random form types not ["Circle","Square"] 
'''
#prevent type two
def factory(type):
    class Circle():
        def draw(self): print("Circle.draw")
        def erase(self): print("Circle.erase")

    class Square():
        def draw(self): print("Square.draw")
        def erase(self): print("Square.erase")

    if type == "Circle": return Circle()
    if type == "Square": return Square()
    assert 0, "Bad shape creation: " + type

def shapeNameGen(n):
    for i in range(n):
        data_random=random.choice(["Circle", "Square"])
        print("in shapeNameGen random choice"+data_random)
        yield factory(data_random)

#-------can specify call with--------------
def select_draw_circle():
    factory("Circle").draw()
#------------------------------------------

#Circle() # Not defined
#print "Circle Defined Direct Creation"
#Circle().draw()
#Circle().erase()
print("in select_draw_circle")
select_draw_circle()

print("in loop")
for shape in shapeNameGen(7):
    shape.draw()
    shape.erase()