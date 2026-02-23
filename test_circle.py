import pytest
import shapes
import math

class TestCircle:
    
    def setup_method(self,method):
        print("Setting up {}".format(method))
        self.circle = shapes.Circle(10)
        
        
    def teardown_method(self,method):
        print("Tearing down {}".format(method))
        
    
    def test_area(self):
        
        assert self.circle.area() == math.pi * self.circle.radius ** 2
        
    def test_perimeter(self):
        
        assert self.circle.permiter() == math.pi * self.circle.radius * 2
        
    def test_not_same(self,my_rectangle):
        assert self.circle.area() != my_rectangle.area()
        
    