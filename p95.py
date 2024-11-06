#   This function finds all even numbers within a given range.


def find_even_numbers(start, end):
    even_numbers = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
