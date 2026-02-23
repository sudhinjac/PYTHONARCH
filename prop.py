"""
Sometimes a value should look like a variable
but actually be calculated dynamically.
Notice: We didn’t call total_value()
It behaves like an attribute
But it runs a method internally
Why This Is Useful
Encapsulation
Hide logic behind clean interface
Calculate values dynamically
Validation
    """



class Stock:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    @property
    def total_value(self):
        return self.price * self.quantity
    
s = Stock(100, 5)
print(s.total_value)