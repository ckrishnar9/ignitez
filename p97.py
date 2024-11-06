#  Write a program to find all the factors of a given number using for loop.


def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors
