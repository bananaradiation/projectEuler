numbers = []
for x in xrange(1000):
	if x % 3 == 0 or x % 5 == 0:
		numbers.append(x)
print sum(numbers)
