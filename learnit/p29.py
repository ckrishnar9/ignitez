# Write a program to remove all elements from a list that are not in another list. 

lst = [83,34,45,46,57,34,34,67,76,89,34,78,6]

n_lst = [25, 35, 45, 55, 34]

filter_list = list(filter(lambda x:x in n_lst, lst))

print(filter_list)