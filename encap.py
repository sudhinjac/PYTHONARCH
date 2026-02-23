class Product:
    
    def __init__(self):
        
        self.__productId = " "
        self.__productName = " "
        self.__price = " "
        
    def updatePrice(self,price):
        self.__price = price
    def setProduct(self,pid,pname,price):
        
        self.__productId = pid
        self.__productName = pname
        self.__price = price
        
    def showProduct(self):
        
        print("Product id: {}\nProduct Name : {}\nPrice : {}".format(
            self.__productId,self.__productName,self.__price
        ))
        
tv = Product()

tv.setProduct("TV101", " LG Golden Eye", 185000)
tv.showProduct()
tv.updatePrice(9500)
tv.showProduct()
        