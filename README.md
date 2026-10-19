Triangle Classifier 

Project Overview:

The project validates triangles based on their three side lengths. It identifies invalid triangles, equilateral, isosceles, and scalene triangles, and flags right triangles by adding the "Right " prefix to their classification.

The following test covers:

Triangle inequality boundary cases, such as (1, 1, 2), which must return "Invalid".
Equilateral, isosceles, and scalene classifications.
Right triangles, including checking that the result includes the "Right " prefix.

How to run the project: 

Install the following dependencies:
python -m pip install -r requirements.txt
Run all tests:
python -m pytest -v

Copilot Review Log: 

1. In triangle.py, Copilot suggested "not a triangle" when the assignment specifically asked for "Invalid" so I changed that to meet the requirement. 
2. In test_tiriangle.py Copilot suggested (1, 1, 2) == "Isosceles"
However, the triangle inequality was not satisfied for Isocceles because the third side has to be greater than the two equal sides. So, I edited it to match that criteria. 
3. In test_triangle.py Copilot suggested (1, 2, 3) == "Scalene" 
Edited to (2, 3, 4) because (1, 2, 3) does not form a triangle. 
4. In test_triangle.py, edited prefix to "Right Scalene" instead of "Right" which Copilot suggested inititally. 

Implementation Note:

An Equilateral triangle can never be classified as a right triangle because an equilaterl triangle has three equal angles which measure 60 degrees. In order for a triangle to be right it must measure 90 degrees on at least one angle.

Acceptance Criteria:

1. Invalid triangle inputs return "Invalid" instead of crashing the program.
2. Valid triangle inputs return the correct classification.
3. Right triangle uses the prefix "right" so the studio can ensure if a corner needs to be corrected.

AI Use Disclosure:

ChatGPT was used to guide step by step on how to get started and explaining the assignment. It was also used to help with the README.md. Copilot was used to generate suggestions which were edited to ensure they meet the requirements for the assignment. 