import pytest
import shapes

@pytest.mark.parametrize("length, expected_area",[(5,25),(4,16),(3,9),(9,81)])
def test_mul_sq(length,expected_area):
    
    assert shapes.Square(length).area() == expected_area
    


@pytest.mark.parametrize("length, expected_per",[(5,20),(4,16),(3,12),(9,36)])
def test_mul_per(length,expected_per):
    
    assert shapes.Square(length).perimeter() == expected_per
    