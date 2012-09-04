# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all primes below two million

import math

def sumPrimes(n):
	sum = 2
	for i in xrange(3, n, 2):
		if all(i % num != 0 for num in xrange(2, 
				int(math.sqrt(i)) + 1 )):
			sum += i
			print sum
	return sum

print sumPrimes(2000000)
