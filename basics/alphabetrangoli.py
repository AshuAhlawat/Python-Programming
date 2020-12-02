from typing import Sized


def print_rangoli(size):
    char = 'abcdefghijklmnopqarstuvwxyz'[0:size]
    for i in range(size-1, -size, -1):
        x = abs(i)
        if x >= 0:
            line = char[size:x:-1]+char[x:size]
            print("--"*x+'-'.join(line)+"--"*x)


input1 = int(input("Enter the sizew of the rangoli here: "))
print_rangoli(input1)
