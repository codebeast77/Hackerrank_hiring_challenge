from math import sqrt


def get_minimum_unique_square(x,y):
    "write your solution here"
    count = 0
    for num in range(x, y + 1):
        if sqrt(num).is_integer():
            count += 1
    return count
