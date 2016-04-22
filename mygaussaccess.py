#iteration demo in gaussian elimination 
n=5
for k in range(0,n):
		print " For k ", k
		print " During Division Step "
		for j in range(k+1, n):
			print "accessing A[{0},{1}]=A[{4},{5}]/A[{2},{3}]".format(k,j,k,k,k,j)
		print " During elimination "
		for i in range(k+1, n):
			for j in range(k+1,n):
					print "accessing A[{0},{1}]=A[{2},{3}]-A[{4},{5}]*A[{6},{7}]".format(i,j,i,j,i,k,k,j) 
