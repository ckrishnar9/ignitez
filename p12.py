#  Write a program to merge two lists and sort them. 

my_list1 = [23,545,23,45,23,57,834,67]
my_list2 = [23,545,283,415,22,547,84,6]

my_list1.extend(my_list2)
my_list1.sort()
print(my_list1)