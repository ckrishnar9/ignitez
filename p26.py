# Write a program to remove all elements from a list that are divisible by a given number. 

lst = [83,34,45,46,57,34,34,67,76,89,34,78,6]

n = 3

# out = list(filter(lambda x:x%n != 0, lst))

out = [i for i in lst if i%n != 0]


print(out)