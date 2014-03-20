# Dynamic programming solution for rod cutting problem
# length of rod
length = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# price for rod of length i
price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

# cut rod of length n and return total price
def cut_rod(price, n):
	mem = [0] * n
	for l in xrange(1, n + 1):
		m = price[l-1]
		for s in xrange(1, l):
			# we already have a solution for subproblem
			m = max(m, mem[s-1] + mem[l-s-1])
		# memorize
		mem[l-1] = m
	print mem
	return mem[n-1]

cut_rod(price, 10)