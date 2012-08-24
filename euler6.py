# Find the difference between the sum of the squares of 
# the first one hundred natural numbers and the 
# square of the sum.

def sum_sq_diff(n):
   squares, sums = [], []
   for x in xrange(n):
      squares.append(x**2)
      sums.append(x) 
   return sum(sums)**2 - sum(squares)

print sum_sq_diff(101)

