# Converts Ax=b into Ux=y
import numpy as np
def gaussian_elimintation(A,b): 
	y = np.zeros(b.shape)
	n=A.shape[0]
	for k in range(0,n):
		print " For k ", k
		for j in range(k+1, n):
			A[k,j]=A[k,j]/A[k,k]
		y[k]=b[k]/A[k,k] 
		A[k,k]=1
		print " After Division A\n", A
		print " After Division b\n", b
		for i in range(k+1, n):
			for j in range(k+1,n):
					A[i,j]=A[i,j]-A[i,k]*A[k,j] 
			print "Elimination step A\n", A
			b[i]=b[i]-A[i,k]*y[k]
			print "Elimination step B\n", b
			A[i,k]=0
	print "finally"
	print "A \n", A
	print "y \n", y


def file_reader(filename): 
	with open(filename) as _file:
		lines = _file.readlines()
	A=np.array(map(lambda line: [float(s) for s in line.split()], lines ))
	return A

if __name__ == '__main__':	
	A = file_reader("/Users/josyulakrishna/Desktop/Dense Matrix Algorithms/3x3.in")
	b=A[:,-1]
	A = A[:,:-1]
	print "intially A is \n",A , " intially b is ",b
	gaussian_elimintation(A,b)