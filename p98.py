#  Write a program to find all the divisors of a given number using for loop.

def find_divisors(number):
    divisors = []
    
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
            
    return divisors