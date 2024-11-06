#  Write a program to find all the common elements in two lists using for loop.


def find_common_elements(list1, list2):
    common_elements = []
    
    for item in list1:
        if item in list2 and item not in common_elements:
            common_elements.append(item)
            
    return common_elements
