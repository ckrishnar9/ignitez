# Write a program to check if a list is palindrome. 

def palindrome_check(a_list):
    if a_list == a_list[::-1]:
        print("It is a palindrome")
    else:
        print("Not")


palindrome_check([23,12,23])