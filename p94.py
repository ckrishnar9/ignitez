# Write a program to find all the odd numbers between a given range using for loop.


def find_odd_numbers(start, end):
    odd_numbers = []
    for num in range(start, end + 1):
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers
