# Write a program to find the second largest element in a list. 

my_list = [1,2,3,18,4,24,5]

first_large, second_large = float('-inf'), float('-inf')

for i in my_list:
    if i > first_large:
        second_large = first_large
        first_large = i
    elif i > second_large and i <= first_large:
        second_large = i

print(second_large)