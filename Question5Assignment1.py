# Question 5

import math

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    if type(radiusOfCircle1) != int or type(radiusOfCircle1) != int:
        return "Error: Both radii should be integers!"
    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
        return "Error: Both radii should be positive!"

    area_of_circle_1 = math.pi * (radiusOfCircle1 ** 2)
    area_of_circle_2 = math.pi * (radiusOfCircle2 ** 2)

    if area_of_circle_1 < area_of_circle_2:
        smaller_area = area_of_circle_1
        larger_area = area_of_circle_2

        percentage_of_larger_circles_area_that_can_be_covered_by_the_smaller_circle = (smaller_area / larger_area) * 100
        return percentage_of_larger_circles_area_that_can_be_covered_by_the_smaller_circle

percentage_covered_by_smaller_circle_for_the_valid_radii = circleAreaCoverage(3,5)
print("The percentage of the larger circle covered by the smaller circle is", percentage_covered_by_smaller_circle_for_the_valid_radii)

percentage_covered_by_smaller_circle_for_the_valid_radii = circleAreaCoverage(4, -7)
print("The result for the invalid radii input: ", percentage_covered_by_smaller_circle_for_the_valid_radii)