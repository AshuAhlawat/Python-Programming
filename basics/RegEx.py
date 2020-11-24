#this is a library to use eith character and metacharacter
import re
txt = "the rain in spain"
x = re.search("portugal", txt)
y = re.search("ai", txt)
z = re.findall("ai", txt)
m = re.sub("rain", "lodu lalit", txt)
print(x)
print(y)
print(z)
print(m)
