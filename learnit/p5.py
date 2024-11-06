# Write a program to find the median of all elements in a list. 

elements_list = [21,34,57,1,32,33,34,35,36,37,38,54,45,6,56,41,1,1,1,2,3,4,5,6]

elements_list.sort()

print(elements_list)

if len(elements_list)%2 == 0:
    median_i = int(len(elements_list)+1)//2
    print(elements_list[median_i])
else:
    median_i1 = len(elements_list)//2-1
    median_i2 = len(elements_list)//2
    median_i =  (elements_list[median_i1] + elements_list[median_i2])//2
    print(elements_list[median_i])
