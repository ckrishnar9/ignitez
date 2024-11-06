#  Write a program to find all the ugly numbers between a given range using for loop.


def find_ugly_numbers(start, end):
    ugly_numbers = []
    for num in range(start, end + 1):
        if is_ugly(num):
            ugly_numbers.append(num)
    return ugly_numbers


def is_ugly(num):
    if num <= 0:
        return False
    for i in [2, 3, 5]:
        while num % i == 0:
            num //= i
    return num == 1
