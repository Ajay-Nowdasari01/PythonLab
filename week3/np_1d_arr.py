import numpy as np
npLst = np.array([2,4,5,6,56,7])
print("values in the list: ",npLst)
print("Array Type:",type(npLst))
print("value at index -2: ",npLst[-2])  #here we can use negative indexing
print("value at index 2: ",npLst[2])
print("values at index 3 to 5: ",npLst[3:5])
print("Slice from index start to 3: ",npLst[:3]) 
print("Slice from index 3 to end: ",npLst[3:])
print("Every other element:",npLst[::2])
print("Reversed array : ",npLst[::-1] ) # Reverse the array
# we can observe many types of slicing
print("Sum of array elements: ",np.sum(npLst))
print("Mean of array elements: ",np.mean(npLst))
print("Maximum element: ",np.max(npLst))

a=np.ndarray(3,int, npLst)
print(a)
