from triangle import classify_triangle


def test_classify_triangle():
    #returns invalid instead of crashing
    assert classify_triangle(1, 1, 2) == "Invalid"
    #validates that the triangle is equilaterlal
    assert classify_triangle(3, 3, 3) == "Equilateral"
    #validates that the triangle uses the prefix "Right" for right triangles
    assert classify_triangle(3, 4, 5) == "Right Scalene"
