from dataclasses import dataclass

@dataclass
class Trade:
    symbol: str
    quantity: int
    
    
    """
    Now you cannot change attributes.
Good for:
Results
Config objects
Financial records
   
    """