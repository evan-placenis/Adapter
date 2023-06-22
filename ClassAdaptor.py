from abc import ABC, abstractmethod
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
#Class ADAPTER
class TextShape(Shape, TextView):
    def __init__(self):
        
        pass
    
    #convert Textview's interface to conform to Shape's
    def BoundingBox(self, bottomLeft: Point, topRight: Point):
        bottom = Coord()
        left = Coord()
        width = Coord()
        height = Coord()

        self.GetOrigin(bottom,left)
        self.GetExtent(width, height)

        bottomLeft = Point(bottom, left)
        #topRight = Point(bottom+height, left+width)


    def IsEmpty():
        textV = TextView()
        return textV.IsEmpty()
    
    def CreateManipulator():
        manipulator = TextManipulator()
        return manipulator
    



    
    
