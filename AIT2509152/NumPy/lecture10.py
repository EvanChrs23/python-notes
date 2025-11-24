import numpy as np
import sys

arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0)
print(r1)

output = np.ones((5,5))
z = np.zeros((3,3))
z[1,1] = 3
output[1:-1,1:-1] = z
print(output)


a = np.array([1,2,3,4])
print(a+2)

stats = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for i in range(3):
    print(np.max(stats, axis=i))

c = np.arange(-9, -3).reshape(2,3)
print(c)
print(c.swapaxes(0,1))
print(c.transpose())

d = np.arange(0,100)
print(d)
print(d.dtype)
print(d.nbytes)
d = np.arange(0,100, dtype='int8')
print(d)
print(d.dtype)
print(d.nbytes)

n = 1000000
print(n.bit_length())
print(type(n))
print(sys.getsizeof(n))
o = np.array([n])
print(o.dtype)
print(o.itemsize)

e = np.array([[3.1415926,2,3],[4,5,6]])
print(e)
print(e.dtype)
np.set_printoptions(precision=5,suppress=True) #only changing the display of 3.1415926 into 3.14159
print(e)
e = e.round(decimals=4) #changes the value of 3.1415926 into 3.14
print(e)