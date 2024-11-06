# Write a program to find all the happy numbers between a given range using for loop.


def sum_square_digits(n):
  """Calculates the sum of the squares of the digits of a number."""
  sum = 0
  while n > 0:
    digit = n % 10
    sum += digit * digit
    n //= 10
  return sum

def is_happy_number(n):
  """Checks if a number is a happy number."""
  seen = set()
  while n != 1 and n not in seen:
    seen.add(n)
    n = sum_square_digits(n)
  return n == 1

def find_happy_numbers_in_range(start, end):
  """Finds all happy numbers within a given range."""
  happy_numbers = []
  for num in range(start, end + 1):
    if is_happy_number(num):
      happy_numbers.append(num)
  return happy_numbers