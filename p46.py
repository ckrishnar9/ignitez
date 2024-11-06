#  Write a program to sort a dictionary by key.

dict1 = {
    "c": 41,
    "a": 23,
    "b": 45,
}

sorted_dict = dict(sorted(dict1.items()))

print(sorted_dict)