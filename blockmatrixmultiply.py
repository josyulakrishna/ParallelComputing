import numpy as np
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
b=a 
print np.dot(a,b)
a00=np.array([[1,2],[5,6]])
a01=np.array([[3,4],[7,8]])
a10=np.array([[9,10],[13,14]])
a11=np.array([[11,12],[15,16]])
print " a00 ", a00
b00=a00
b01=a01
b10=a10
b11=a11
print " b00 \n ", b00
print "c00 = a00b00 + a01b10"
print np.dot(a00,b00)+np.dot(a01,b10)
