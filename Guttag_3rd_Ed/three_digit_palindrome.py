# Project Euler - problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit number

# use a recursive function to check if the next number is a palindrome
def check_if_palindrome(number):
	number =str(number)
	if len(number) <=1:
		return True
	else:
		return number[0] == number[-1] and check_if_palindrome(number[1:-1])
	

def is_pal():
	highest = 1
	for x in range(100, 1000):
		for y in range(100, 1000):
			if check_if_palindrome(x * y) and x * y > highest:
				highest = x * y
	return highest

print(is_pal())

