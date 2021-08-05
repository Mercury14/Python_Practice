# Write a function that accepts two strings as arguments and returns True if either string occurs anywhere in the other and False otherwise.

def isIn(string_1, string_2):
    """
    A function that accepts two strings as arguments and returns True if either string occurs anywhere in the other and False otherwise"""


    if string_1 in string_2 or string_2 in string_1:
        return True

    else:
        return False



x = input("Enter the first string ")
y = input("Enter the second string ")
print(isIn(x, y))