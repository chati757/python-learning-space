import random
#Advantages is not define many place when create new shap
class ShapeFactory:
    factories = {} #<maybe this line adapt to database

    def addFactory(id, shapeFactory):
        print("in addFactory shapeFactory get in ShapeFactory.factories.put["+id+"]")
        ShapeFactory.factories.put[id] = shapeFactory
    addFactory = staticmethod(addFactory)

    # A Template Method:
    def createShape(id):

        print("in createShape at :"+id)
        print("all key after createShape",ShapeFactory.factories)
        print("pre if",ShapeFactory.factories.has_key(id))

        if not ShapeFactory.factories.has_key(id):
            print("in if")
            ShapeFactory.factories[id] = \
              eval(id + '.Factory()')
            print("eval this:",id + '.Factory()')
            print("return creation")
        return ShapeFactory.factories[id].create()

    createShape = staticmethod(createShape)

class Shape(object): pass

class Circle(Shape):
    def draw(self): print("Circle.draw")
    def erase(self): print("Circle.erase")
    class Factory:
        def create(self): return Circle()

class Square(Shape):
    def draw(self):print("Square.draw")
    def erase(self):print("Square.erase")
    class Factory:
        def create(self): return Square()

class Erase():
    def all(self):print("erase all")
    class Factory:
        def create(self): return Erase()

def shapeNameGen(n):
    types = Shape.__subclasses__()
    print("in shapeNameGen",types)
    for i in range(n):
        yield random.choice(types).__name__

#print("direct call") #this Factory not prevent direct creation
#Circle().draw()
#Circle().erase()

#-------can specify call with--------------
def specify_call():
    print("specify mode")
    ShapeFactory.createShape("Circle").draw()
    ShapeFactory.createShape("Erase").all()
#------------------------------------------
specify_call()

#retun line in createShape must outside if condition
#if wanna use in loop, below this
print("in loop")
shapes = [ShapeFactory.createShape(i)
           for i in shapeNameGen(7)]

for shape in shapes:
    shape.draw()
    shape.erase()