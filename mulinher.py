class Father:
    
    def fatherProperty(self):
        print("Father Property")
        
class Mother:
    
    def motherProperty(self):
        print("Mother Property")
        
class Child(Father, Mother):
    def property(self):
        print("Child will inherit: ")
        super().fatherProperty()
        super().motherProperty()
        
c1 = Child()
c1.property()