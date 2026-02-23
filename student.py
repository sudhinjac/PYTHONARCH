class Test:
    
    staticVariable = 0
    instanceVariable = 0
    
    
    def __init__(self):
        print("Constructing the object for the test class")
        self.instanceVariable +=1
        Test.staticVariable += 1
        
        
t1 = Test()
print("After creating first object: ")
print("Instance variable: ",t1.instanceVariable)
print("Static Variable: ",t1.staticVariable)

t2 = Test()
print("After creating first object: ")
print("Instance variable: ",t1.instanceVariable)
print("Static Variable: ",t1.staticVariable)
print("static Variable using Class ref. : ", Test.staticVariable)