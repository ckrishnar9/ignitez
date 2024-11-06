# Write a program to rotate a list by a given number of positions. 

lst = [83,34,45,46,57,34,34,67,76,89,34,78,6]

n = 3

n = n % len(lst)

rotated_lst = lst[n:] + lst[:n]

print(rotated_lst)