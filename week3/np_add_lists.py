import numpy as np
lst1=[1,2,3,4,5]
lst2=[6,7,8,9,10]
print(lst1+lst2)
npLst1= np.array(lst1)
npLst2= np.array(lst2)
print("addition",npLst1+npLst2)
print("subtraction",npLst1-npLst2)
print("multiplication",npLst1*npLst2)
print("exponentation",npLst1**npLst2)
print("division",npLst1/npLst2)
print("floor division",npLst1//npLst2)
print("modulous",npLst1%npLst2)
