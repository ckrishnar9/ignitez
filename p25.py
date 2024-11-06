# Write a program to remove all duplicates from a list

lst = [83,34,45,46,57,34,34,67,76,89,34,78,6]

new_lst = list(set(lst))

print(new_lst)

another_lst = dict.fromkeys(lst)
print(another_lst.keys())