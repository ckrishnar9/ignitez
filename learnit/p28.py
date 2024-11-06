# Write a program to remove all elements from a list that are greater than a given number. 

lst = [83,34,45,46,57,34,34,67,76,89,34,78,6]

num = 67

out = list(filter(lambda x:x >= num, lst))

print(out)