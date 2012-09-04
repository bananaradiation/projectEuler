# 2520 is the smallest number that can be divided by 
# each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly 
# divisible by all of the numbers from 1 to 20?

import math
import numpy

''' pseudo-code:
	num = 20
	1. multiples = [2]
	2. for i in xrange(3, num):
		a. make [prime factorization] for i
		b. diff([mult], [pf])
		c. multiples.append([diff])
	3. return prod(multiples)
'''
