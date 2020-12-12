import numpy as np
#LCM part
num1=4
num2=8
print(np.lcm(num1,num2))

arr=np.array([[2,4,8,16,36],[3,6,9,12,15],[5,10,15,20,25]])

print(np.lcm.reduce(arr))
#GCD part
num1=3
num2=6
print(np.gcd(num1,num2))

arr=np.array([20,24,16,36,32,64])
print(np.gcd.reduce(arr))