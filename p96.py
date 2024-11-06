#  Write a program to find all the perfect squares between a given range using for loop.

import math


def find_perfect_squares(start, end):
    perfect_squares = []
    for num in range(start, end + 1):
        sqrt_num = int(math.sqrt(num))
        if sqrt_num * sqrt_num == num:
            perfect_squares.append(num)
    return perfect_squares
