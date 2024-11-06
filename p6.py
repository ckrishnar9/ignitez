# Write a program to remove all duplicates from a list.

element_list = [1,2,3,4,5,6,7,8,1,2,3]

# no_dups = list(set(element_list))

# print(no_dups)

no_dups = []

for i in element_list:
    if i not in no_dups:
        no_dups.append(i)

print(no_dups)