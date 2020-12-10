import math
c=complex(input())
real=abs(c.real)
imag=abs(c.imag)
x=math.sqrt((real)**2 + (imag)**2)
print(x)
if real==0:
    y=(math.pi/2)
else:
    y=math.atan((imag)/(real))
print(round(y,5))
print(round(y*180/math.pi),"Degree")