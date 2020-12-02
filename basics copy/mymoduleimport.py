#By this 
from mymodule import person1
import mymodule as mx
a = mx.person1["age"]
b = mx.person1["name"]
c = mx.person1["country"]
d = dir(mx)
print(d)
print(a)
print(b)
print(c)

print(person1["age"])
