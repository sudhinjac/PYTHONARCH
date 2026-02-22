class Point:
    
    def __init__(self,x,y):
        self.X = x
        self.Y = y
        
    def __add__(self,other):
        
        x = self.X + other.X
        y = self.Y + other.Y
        
        return Point(x,y)
    
    def  __str__(self):
        return "( {0}, {1})".format(self.X,self.Y)
    
    
p1 = Point(10,25)
p2 = Point(10,10)

result = p1 + p2
print(result)