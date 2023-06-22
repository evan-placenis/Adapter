from abc import ABC, abstractmethod

class Coord():
    def __init__(self):
        pass
class Point():
    def __init__(self, c1: Coord, c2: Coord):
        pass

class TextManipulator():
    #suppors manipulator of a TextShape
    pass

class Shape(ABC):
    
    @abstractmethod
    def BoundingBox(bottomLeft:Point, topRight:Point):
        print("Setting box with points")

    @abstractmethod
    def CreateManipulator():
        pass

class TextView(ABC):

    def GetOrigin(self, x:Coord, y: Coord):
        print("Setting origin of box with Coordinates")

    def GetExtent(self, width: Coord, height: Coord):
        print("Setting width/height of box with Coordinates")
    
    def IsEmpty():
        pass

#-------------------------------------------------------------------------------
#Object ADAPTER
class TextShape(Shape):
    def __init__(self, t:TextView):
        self.text = t
    
    def BoundingBox(self, bottomLeft: Point, topRight: Point):
        bottom = Coord()
        left = Coord()
        width = Coord()
        height = Coord()
        

        self.text.GetOrigin(bottom,left)
        self.text.GetExtent(width, height)

        bottomLeft = Point(bottom, left)
        #topRight = Point(bottom+height, left+width)


    def IsEmpty(self):
        return self.text.IsEmpty()
    
    def CreateManipulator():
        manipulator = TextManipulator()
        return manipulator
    
#-------------------------------------------------------------------------------
#CLIENT
test = TextView()
t = TextShape(test)
c1 = Coord()
c2 = Coord()
c3 = Coord()
c4 = Coord()
p1 = Point(c1,c2)
p2 = Point(c3,c4)
t.BoundingBox(p1, p2)

