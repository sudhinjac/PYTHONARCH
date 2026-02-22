class English:
    
    def greet(self, name):
        print("Good Morning ",name)
        
class French:
    def greet(self,name):
        print("Bonjour ",name)
        
def greetings(language, name):
    language.greet(name)
    
e = English()
f = French()

greetings(e,"Sudhin")
greetings(f,"sudhin")