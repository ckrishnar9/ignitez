# Write a program to find the difference between two lists. 

lst1 = [83,34,45,46,57,34,34,67,76,89,34,78,6]
lst2 = [23,34 ,545,283,415,22,547,84,6]

res = [i for i in lst1 if i not in lst2]

print(res)