from abc import ABC, abstractmethod


class Institutes(ABC):
    
    def __init__(self):
        print(type(self).__name__, " detials :")
        
    def courseOffered(self):
        print("Courses offered are C, C++, Java")
        
    @abstractmethod
    def address(self): pass
    
    
class techAcademy(Institutes):
    
    def courseOffered(self):
        print("Courses offered : Python, ML, Databases")
        
    def address(self):
        print("Address @ Hyderbad")
        
class onlineAcademy(Institutes):
    def address(self):
        print("Address @ Bangalore")
        
ta = techAcademy()
ta.courseOffered()
ta.address()

olt = onlineAcademy()
olt.courseOffered()
olt.address()