# Write a program to sort a list in ascending order. 


def bubble_sort(original_list):
    n = len(original_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if original_list[j] > original_list[j+1]:
                original_list[j], original_list[j+1] = original_list[j+1], original_list[j]
    return  original_list

# Example usage:
my_list = [34, 12, 5, 78, 23]
sorted_list = bubble_sort(my_list)
print("Sorted list:", sorted_list)