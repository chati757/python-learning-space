
import random

class Shape(object):
    # Create based on class name:
    def factory(type):
        #return eval(type + "()")
        if type == "Circle": return Circle()
        if type == "Square": return Square()
        assert 0, "Bad shape creation: " + type
    factory = staticmethod(factory)#factory must have this

class Circle(Shape):
    def draw(self): print("Circle.draw")
    def erase(self): print("Circle.erase")

class Square(Shape):
    def draw(self): print("Square.draw")
    def erase(self): print("Square.erase")

# Generate shape name strings:
def shapeNameGen(n):
    types = Shape.__subclasses__()
    print("sub class..")
    print types,"\n" #EX.[<class '__main__.Circle'>,<class '__main__.Square'>]

    rc_type=random.choice(types)
    print "random choice example is",rc_type,"name is ",rc_type.__name__,"\n"
    for i in range(n):
        #yield is generator and return iterator
        yield random.choice(types).__name__

# call section
# \ can be using make paragraph of code form shapes = [ Shape.factory(i) for i in shapeNameGen(7)]
#Shape is name of factory class **this 40 line is continue 41 like > shapes = [Shape.factory(i) for i in shapeNameGen(7)]
print "Circle Defined Direct Creation"
Circle().draw()
Circle().erase()

shapes = \
[Shape.factory(i) for i in shapeNameGen(7)] #i = name of type random shapeNameGen ex Circle , Square
for shape in shapes:
    print("shape")
    print(shape)
    print("shapes")
    print(shapes)
    shape.draw()
    shape.erase()