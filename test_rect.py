import pytest



def test_area(my_rectangle):
    
    assert my_rectangle.area() == 10 * 20
    
def test_perimer(my_rectangle):
    
    assert my_rectangle.perimeter() == 2 * 30
    
def test_not_equal(my_rectangle,w_rectangle):
    assert my_rectangle != w_rectangle