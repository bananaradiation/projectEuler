# There exists exactly one Pythagorean triplet for which
# a + b + c = 1000. Find the product abc

def pythagorean(max):
	for n in xrange(1, max):
		for m in xrange(1, n):
			a = n**2 - m**2
			b = 2 * n * m
			c = n**2 + m**2
		
			if a + b + c == 1000:
				return a*b*c

print pythagorean(50)
