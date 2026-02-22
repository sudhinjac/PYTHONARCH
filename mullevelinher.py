class GrandParents:
    
    def propertyLand(self):
        
        print("Property Land Given for farming by Grand Parents\n")
        

class Parents(GrandParents):
    def propertyHome(self):
        print("Poperty home constructed by Parents")
        
class Child(Parents):
    def propertyVehicle(self):
        print("Property Car purchased by Child")
        
    def propertyLand(self):
        print("Land taken for commercial use\n")
        
c1 = Child()

c1.propertyLand()
c1.propertyHome()
c1.propertyVehicle()
