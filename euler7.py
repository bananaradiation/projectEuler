import math

def primeOrder(n):
	count = 1
	for i in xrange(3, n, 2):
		if all(i % num != 0 for num in xrange(2, 
				int(math.sqrt(i)) + 1 )):
			count += 1
		if count == 10001:
			return i, count
			break

print primeOrder(200000)
