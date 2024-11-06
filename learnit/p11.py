# Write a program to find the second smallest element in a list. 

my_list = [2,3,4,5,6,34,456,345,45]

first_small, second_small = float("inf"), float("inf")

for i in my_list:
    if i < first_small:
        second_small = first_small
        first_small = i
    elif i < second_small and i != first_small:
        second_small = i

print(second_small) 