q = 2
for i in range(0,q):
	for j in range(0,q):
		print "computing C[{0},{1}]".format(i,j) 
		for k in range(0,q):
			print "A[{0},{1}]*B[{2},{3}]".format(i,k,k,j)
