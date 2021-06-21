

def largest_prime_factor(num):
	n = 2

	while (n * n < num):
		while (num % n ==0):
			num = num / n
		n=n+1
	
	return (int(num))


print(largest_prime_factor(600851475143))
print(largest_prime_factor(10))
