# Write a function that accepts two strings as arguments and returns True if either string occurs anywhere in the other and False otherwise.

# Capture first string
string_1 = input("Enter the first string ")
string_2 = input("Enter the second string ")

if string_1 in string_2:
    print("True")

elif string_2 in string_1:
    print("True")

else:
    print("False")
