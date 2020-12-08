import math
ab=float(input("Enter the value of AB: "))
bc=float(input("Enter the value of BC: "))
bm=((ab/2)**2+(bc/2)**2)**(1/2)
angle=math.asin(bm/bc)
theta=angle*180/math.pi
print(round(theta),'°',sep='')