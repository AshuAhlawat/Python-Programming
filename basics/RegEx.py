import re
from typing import Text
txt = "the rain in spain"
x = re.search("portugal", txt)
y = re.search("spain", txt)
z = re.findall("ai", txt)
m = re.sub("ai", "(lodu lalit)", txt)
print(x)
print(y)
print(z)
print(m)
