import numpy

arr=numpy.array([2,1,3,6,5,8,7,9,10,4])
even=numpy.where(arr%2==0)
newarr=[]
for i in even[0]:
    newarr.append(arr[i])
newarr.sort()
m=int(input("enter the number of inputs: "))
list1=[]
for i in range(m):
    n=int(input("enter the number: "))
    list1.append(n)
print(list1)
for i in range(len(list1)):
    x=numpy.searchsorted(newarr,list1[i])
    newarr.insert(x,list1[i])
print(newarr)