# Write a program to remove all elements from a list that are less than a given number. 

lst = [83,34,45,46,57,34,34,67,76,89,34,78,6]

n = 10

out = [i for i in lst if i >= n]

print(out)