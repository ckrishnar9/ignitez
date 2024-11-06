# Write a program to find all the Smith numbers between a given range using for loop.


def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def prime_factors(n):
    factors = []
    i = 2
    while n > 1:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    return factors


def is_smith_number(n):
    if n <= 1:
        return False

    sum_of_digits = sum_digits(n)
    prime_factor_sum = sum(sum_digits(factor) for factor in prime_factors(n))
    return sum_of_digits == prime_factor_sum


def find_smith_numbers_in_range(start, end):
    smith_numbers = []
    for num in range(start, end + 1):
        if is_smith_number(num):
            smith_numbers.append(num)
    return smith_numbers
