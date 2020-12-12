import numpy as np


trigo=['sin','cos','tan']
arr=np.array([np.pi,np.pi/2,np.pi/3,1.5*np.pi/2])
for i in trigo:
    print(eval('np.{}(arr)'.format(i)))


angle=np.array([1,0,-1])
trigo=['arcsin','arccos','arctan']
for i in trigo:
    print(eval('np.{}(angle)'.format(i)))

# Value of Hypotenus
base=int(input("Enter the base: "))
perp=int(input("Enter the perpendicular: "))
print(np.hypot(base,perp))