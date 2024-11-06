# Write a program to find the index of an element in a list. 

lst = [83,34,45,46,57,34,34,676.23]

element = 34

# idx = lst.index(element)

idx = [i for i,x in enumerate(lst) if x == element]

print(idx)