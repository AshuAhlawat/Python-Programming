import numpy as np

emplist=[]
for _ in range(int(input("Enter array length: "))):
    emplist.append(int(input()))
print(emplist)

array=np.array(emplist)
newarr=np.cumsum(emplist)
print(newarr[-1])