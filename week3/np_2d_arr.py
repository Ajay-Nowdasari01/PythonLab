import numpy as np
npLst1 = np.array([[2,4,5,6],[6,4,7,3]])
print("Array Type:\n",npLst1)
npLst2 = np.array([[4,6,3,7],[8,5,2,5]])
print("Array Type:\n",npLst2)

print("Array Type:",type(npLst1))
print("shape of the array",np.shape(npLst1))
print("Array Type:",type(npLst2))
print("shape of the array",np.shape(npLst2))

print("addition\n",npLst1+npLst2)
print("multiplication\n",npLst1*npLst2)

print("Element at row 0, column 1 of list 1: ",npLst1[0, 1])
print("First row list 1:", npLst1[0, :])
print("Second column of list 1:", npLst1[:, 0])

print("Sum of all elements in A:", np.sum(npLst1))
print("Max value in each column of A:", np.max(npLst1, axis=0))
print("Mean value in each row of A:", np.mean(npLst1, axis=1))

#max min std mean ndarray array where var