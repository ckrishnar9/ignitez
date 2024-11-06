# Write a program to find all the unique elements in a list using for loop.

def find_unique_elements(input_list):
    unique_elements = []
    
    for item in input_list:
        if item not in unique_elements:
            unique_elements.append(item)
            
    return unique_elements