import math
from say_hey import say_hello


def sum_five_int(a, b, c, d, e):
    return a + b + c + d + e


def is_more_ten(value):
    return "Yes" if value > 10 else "No"


def squer(a, b, c):
    return a ** b ** c


# print(is_more_ten(9))
# print(sum_five_int(1, 2, 3, 4, 5))
# say_hello("Tima")
def bigger_number(a, b, c):
    return max(max(a, b), c)


# print(bigger_number(1,4,3))
def circle_area(radius):
    return math.pi * radius ** 2


print(circle_area(2))
