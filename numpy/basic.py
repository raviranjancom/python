import numpy as np

#np.array([.....])  ---> numpy array
# np.ndim           ---> gives the dimensions of array
# np.shape          --->gives shape [levels, rows, cols]
# np.__version__    ---> returns the versions

li=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])
# array[start: stop: step]  --> 
# print(li[0:3:2])
# print(li[::2, ::2])
array=np.array([1,2,3])
area=np.pi*(array**2)
array[array>2]=100

# Broadcasting in numpy
array1=np.array([[1,2,3,4]])
array2=np.array([[1],[2],[3],[4]])
# print(array1*array2)
table1=np.array([[1,2,3,4,5,6,7,8,9,10]])
table2=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(table1*table2)
