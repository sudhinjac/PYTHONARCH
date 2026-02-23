from matht import add, divide
import pytest
import time
def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
        
@pytest.mark.slow      
def test_very_slow():
    time.sleep(5)
    assert divide(10,5) == 2
    
@pytest.mark.skip(reason="this feature is currently broken")
def test_add_new():
    assert add(1,2) == 3