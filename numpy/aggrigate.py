import numpy as np

array=np.array([[1,2,3,4,5],
                [6,7,8,9,10]])

# print(np.sum(array))
# print(np.mean(array))
# print(np.std(array))
# print(np.var(array))
# print(np.min(array))
# print(np.max(array))
# print(np.argmin(array))
# print(np.argmax(array))
print(np.sum(array, axis=0)) # axis=0  --> for sum of all cols
                             # axis=1  --> for sum of all rows

 