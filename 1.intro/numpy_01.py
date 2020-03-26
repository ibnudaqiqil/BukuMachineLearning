import numpy as np

a = np.arange(15)
b = np.reshape(a,(3,5))

a2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print (a2.shape)
print (a2.transpose())

a3 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

a4 =a2+a3

a5 = a2.dot(a3.reshape(5,2))