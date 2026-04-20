import numpy as np
arr=np.array([[1,2,3],[4,5,6],[11,11,11]])
# print(arr)
arr1=np.array([7,8,9])
# print(arr.ndim)      #Check the diamention of array
# print(arr1.shape)    #Number of element on Array
# print(arr.shape)
# print(arr)
print(arr.ndim)
# print(arr.shape)

print(arr.size)       #size of array

arr=arr.reshape(6,2)
print(arr)