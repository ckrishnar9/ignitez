# Write a program to find the second largest and second smallest elements in a list. 

lst = [83,34,45,46,57,34,34,676]

if lst[0] >  lst[1]:
    largest = lst[0]
    smallest =  lst[1]
else:
    largest = lst[1]
    smallest = lst[0]

second_small = float("inf")
second_large = float("-inf")

for number in lst:
    if number < smallest:
        second_small = smallest
        smallest = number
    elif number > largest:
        second_large = largest
        largest = number
    elif number < second_small and number !=  smallest:
        second_small = number
    elif  number > second_large and number != largest:
        second_large = number

print("Second largest element is:", second_large)
print("Second smallest element is:", second_small) 