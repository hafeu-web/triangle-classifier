#Accepted Copilot's suggestion because it correctly implements the triangle inequality and handles the degenerate boundary case.
import math


def is_valid_triangle(a, b, c) -> bool:
    """
    Check if the given sides can form a valid triangle.

    A triangle is valid if the sum of any two sides is greater than the third side.

    Parameters:
    a (float): Length of the first side.
    b (float): Length of the second side.
    c (float): Length of the third side.

    Returns:
    bool: True if the sides can form a valid triangle, False otherwise.
    """
    return (a + b > c) and (a + c > b) and (b + c > a)

def classify_triangle(a, b, c) -> str:
    """
    Classify the type of triangle based on the lengths of its sides.

    Parameters:
    a (float): Length of the first side.
    b (float): Length of the second side.
    c (float): Length of the third side.

    Returns:
    str: Type of triangle ('Right Scalene', 'Right Isosceles', 'Equilateral', 'Isosceles', 'Scalene') or 'Invalid' if invalid.
    """
    if not is_valid_triangle(a, b, c):
        return "Invalid"
    #Copilot suggested "not a triangle, assignment asked for "Invalid" so I changed it to that.

    shortest, middle, longest = sorted((a, b, c))
    is_right = math.isclose(
        shortest**2 + middle**2,
        longest**2,
        rel_tol=1e-9,
        abs_tol=1e-9,
    )

    if a == b == c:
        classification = "Equilateral"
    elif a == b or b == c or a == c:
        classification = "Isosceles"
    else:
        classification = "Scalene"

    if is_right:
        return f"Right {classification}"
    return classification

