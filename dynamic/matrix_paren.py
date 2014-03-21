from sys import maxint
# dimension of the matrixs
dimension = [(30, 35), (35, 15), (15, 5), (5, 10), (10, 20), (20, 25)]
m = len(dimension)
mem = [[0 for _ in xrange(m)] for _ in xrange(m)]
for l in xrange(2, m + 1):
    for i in xrange(0, m - l + 1):
        j = i + l - 1
        mem[i][j] = maxint
        for k in xrange(i, j):
            mem[i][j] = min(mem[i][j], mem[i][k] + mem[k+1][j] + dimension[i][0] * dimension[k][1] * dimension[j][1])

for m in mem:
	for i in m:
		print '{:>5} '.format(i),
	print ''