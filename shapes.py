import math
class Shape:
    
    def area(self):
        pass
    
    def permiter(self):
        pass
    
    
class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius **2
    
    def permiter(self):
        return 2 * math.pi * self.radius
    
    
class Rectangle:
    
    
     def __init__(self,lg,bt):
         
         self.length = lg
         self.breadth = bt
         
     def __eq__(self,other):
         if not isinstance(other,Rectangle):
             return False
         return self.breadth == other.breadth and self.length == other.length
         
     def area(self):
         return self.length * self.breadth
     
     def perimeter(self):
         
         return 2 *(self.length+self.breadth)
        

class Square(Rectangle):
    
    def __init__(self,length):
        super().__init__(length,length)
        
   
    
    