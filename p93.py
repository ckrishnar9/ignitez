# Write a program to find all the abundant numbers between a given range using for loop.

def find_abundant_numbers(s, e):
    abundant_numbers = []
    for num in range(s, e+1):
        if is_abundant(num):
            abundant_numbers.append(num)
    return abundant_numbers

def is_abundant(number):
    if number <= 0:
        return False
    total  = 0
    for i in range(1, number):
        if number % i == 0:
            total += i
    return total > number

