# Project Euler - problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit number

# Work backwards froms highest possible values
def problem_four():
	for x in range(999, -1):
		for y in range(999, -1):
			number_to_check = x * y
			if check_if_palindrome(number_to_check, 1, -1) == True:
				print(number_to_check)
				break

# use a recursive function to check if the next number is a palindrome
def check_if_palindrome(number, start_index, end_index):
	if (start_index == end_index):
		return True

		if (number[start_index] != number[end]):
			return False

		if (start_index < end_index+1):
			return check_if_palindrome(number, start_index+1, end_index-1)

		return True

# Test
print(problem_four())
