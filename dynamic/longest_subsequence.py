# algorithm to find the longest subsequence 
def longest_subsequece(src, dest):
	m = len(src) + 1
	n = len(dest) + 1
	# memorize the longest subsequence between src[:i] and dest[:j]
	mem = [[0 for _ in xrange(n)] for _ in xrange(m)]
	for i in xrange(1, m):
		for j in xrange(1, n):
			if src[i-1] == dest[j-1]:
				mem[i][j] = 1 + mem[i-1][j-1]
			else:
				mem[i][j] = max(mem[i-1][j], mem[i][j-1])

	print_da(mem, src, dest)

# for printing the array
def print_da(mem, src, dest):
	m, n = len(src) + 1, len(dest) + 1
	for i in xrange(1,m):
		mem[i][0] = src[i-1]
	for i in xrange(1,n):
		mem[0][i] = dest[i-1]
	mem[0][0] = ' '
	for m in mem:
		for j in m:
			print j,
		print ''
	print ''

longest_subsequece('msbanik', 'banik')