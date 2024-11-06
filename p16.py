# Write a program to remove all occurrences of an element from a list. 

lst = [45,58,28,58,26,36,34,23,28]

n = 28

n_lst = list(filter(lambda x:x !=n, lst))

print(n_lst)