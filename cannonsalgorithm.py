import numpy as np
from collections import defaultdict 
p=4
processorarray=defaultdict(list)
for i,j in zip(range(3),range(3)):
	# for j in range(3):
		processorarray[(i,(j-i+np.sqrt(p))%np.sqrt(p))].append("A[{0}{1}]".format(i,j))
 		processorarray[((i-j+np.sqrt(p))%np.sqrt(p), j)].append("B[{0}{1}]".format(i,j))
print processorarray