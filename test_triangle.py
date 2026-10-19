# Test that invalid triangle side lengths are rejected

from triangle import classify_triangle
import math

def test_invalid_triangle():    
    assert classify_triangle(1, 2, 3) == "Invalid"
    assert classify_triangle(0, 1, 1) == "Invalid"
    assert classify_triangle(-1, 1, 1) == "Invalid"
    assert classify_triangle(1, 1, 2) == "Invalid"

# Test that an equilateral triangle is classified correctly
def test_equilateral_triangle():
    assert classify_triangle(1, 1, 1) == "Equilateral"

# Test that an isosceles triangle is classified correctly
def test_isosceles_triangle():
    assert classify_triangle(2, 2, 3) == "Isosceles"
    assert classify_triangle(2, 3, 2) == "Isosceles"
    assert classify_triangle(3, 2, 2) == "Isosceles"


# Test that a scalene triangle is classified correctly
def test_scalene_triangle():
    assert classify_triangle(2, 3, 4) == "Scalene"

# Test that right triangles are classified correctly
def test_right_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    assert classify_triangle(5, 12, 13) == "Right Scalene"
    assert classify_triangle(8, 15, 17) == "Right Scalene"
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"
    
    