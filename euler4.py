# palindromic number reads the same both ways. The largest 
# palindrome made from the product of two 2-digit numbers
# i.e. 9009 = 91 x 99

# Find the largest palindrome made from the 
# product of two 3-digit numbers.


def palin(x):
	palindrome = []
	for a in range(x,0,-1):
		for b in range(x,0,-1):
			product = a * b
			if str(product) == str(product)[::-1]:
				palindrome.append(product)
				break
			else:
				pass
	return max(palindrome)

print palin(999)
