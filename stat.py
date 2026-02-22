"""
Why is this powerful?
Factory methods
Creating objects from files / API responses
Cleaner object creation logic 


"""

class MathUtils:

    @staticmethod
    def calculate_return(start_price, end_price):
        return (end_price - start_price) / start_price
    
print(MathUtils.calculate_return(100, 120))


class Stock:
    def __init__(self, symbol):
        self.symbol = symbol

    @classmethod
    def from_string(cls, text):
        return cls(text.upper())
    
s = Stock.from_string("aapl")
print(s.symbol)   # AAPL