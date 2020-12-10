from numpy import random

#importing any number from 1 to 100

x=random.randint(100)

print(x)

y=random.randint(100, size=(5))

print(y)

z=random.randint(100, size=(3,5))
print(z)

m=random.rand(3,5)
print(m)

n=random.choice([3,5,7,9])
print(n)

o=random.choice([3,5,7,9], size=(3,5))
print(o)

