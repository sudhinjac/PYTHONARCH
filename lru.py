"""
Now repeated calls are fast.
Used for:
Expensive calculations
Pure indicator functions
ML preprocessing    
    """

from functools import lru_cache

@lru_cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(20))